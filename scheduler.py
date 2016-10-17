"""Scheduler module

This module defines the scheduler part of opennms_alarmforwarder
"""

import datetime
import time
from sqlalchemy.sql import exists
import model
from model import ActiveAlarm
from model import ForwardedAlarm
from model import ForwardingRule
from rulematching import RuleEvaluator
from forwarder import Forwarder
from receiver import OpennmsReceiver

class Scheduler(object):

    def __init__(self, config):
        self.__config = config

    def run(self):
        # create objects
        rule_evaluator = RuleEvaluator()

        # scheduling loop
        while True:
            # open ORM session
            orm_session = model.Session()

            # get all configured sources from database
            sources = orm_session.query(model.Source).all()

            # walk through all sources and process alarms
            for source in sources:
                receiver = OpennmsReceiver(source)

                #get alarms from OpenNMS
                alarms_onms = receiver.get_alarms()

                # add/update alarms to/in database table
                for alarm_id in alarms_onms:
                    alarm = alarms_onms[alarm_id]
                    orm_session.merge(alarm)
                # remove non existing alarms from database table
                query_saved_alarms = orm_session.query(model.ActiveAlarm).filter(model.ActiveAlarm.alarm_source==source.source_name).all()
                for alarm_saved in query_saved_alarms:
                    try:
                        alarms_onms[str(alarm_saved.alarm_id)]
                    except:
                        # resolve forwarded alarms
                        for forwarding_entry in alarm_saved.forwarding_entries:
                            if forwarding_entry.forwarded:
                                target = forwarding_entry.rule.target
                                forwarder = Forwarder.create_forwarder(target.target_name, target.target_class, target.target_parms)
                                forwarder.resolve_alarm(alarm_saved)
                        # remove alarm
                        orm_session.delete(alarm_saved)
                orm_session.commit()

            # walk through all active alarms, that are not forwarded yet
            query_filter = ~exists().where(ForwardedAlarm.alarm_id==ActiveAlarm.alarm_id).where(ForwardedAlarm.alarm_source==ActiveAlarm.alarm_source)
            query_non_forwarded_alarms = orm_session.query(ActiveAlarm).filter(query_filter)
            query_rules = orm_session.query(ForwardingRule)
            for alarm_saved in query_non_forwarded_alarms.all():
                for rule in query_rules.all():
                    # check rule matching
                    if rule_evaluator.evaluate_object(rule.rule_match, alarm_saved):
                        # create forwarding
                        forwarded_alarm = ForwardedAlarm(
                            alarm_id=alarm_saved.alarm_id,
                            alarm_source=alarm_saved.alarm_source,
                            rule_id=rule.rule_id,
                            forwarded=False
                        )
                        orm_session.add(forwarded_alarm)
            orm_session.commit()

            # walk through all forwardings, that were not executed yet
            query_forwarding_alarms = orm_session.query(ForwardedAlarm, ActiveAlarm).\
                                      filter(ForwardedAlarm.forwarded==False).\
                                      filter(ForwardedAlarm.alarm_id==ActiveAlarm.alarm_id).\
                                      filter(ForwardedAlarm.alarm_source==ActiveAlarm.alarm_source)
            for alarm_forwarding, alarm_active in query_forwarding_alarms.all():
                # check forwarding of alarms
                time_diff_obj = datetime.datetime.now() - alarm_active.alarm_timestamp
                time_diff_sec = time_diff_obj.days * 86400 + time_diff_obj.seconds
                if time_diff_sec >= 300:
                    # forward alarm
                    target = alarm_forwarding.rule.target
                    forwarder = Forwarder.create_forwarder(target.target_name, target.target_class, target.target_parms)
                    forwarder.forward_alarm(alarm_active)
                    # set forwarded flag
                    alarm_forwarding.forwarded=True
            orm_session.commit()

            # close ORM session
            orm_session.close()

            # wait time limit for the next scheduler run
            time.sleep(30)

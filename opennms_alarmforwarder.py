#! /usr/bin/python3
"""Main module
"""
import model

def main():
    # only test data at the moment
    orm_session = model.Session()
    rule = model.ForwardingRule(rule_match="all", rule_target="TEST")
    alarm = model.ActiveAlarm(alarm_uei="uei.opennms.org/testalarm", alarm_logmsg="A Testalarm has occurred!")
    orm_session.add(alarm)
    orm_session.add(rule)
    orm_session.commit()

    forwarded_alarm = model.ForwardedAlarm(alarm_id=alarm.alarm_id, rule_id=rule.rule_id)
    orm_session.add(forwarded_alarm)
    orm_session.commit()


if __name__ == "__main__":
    main()

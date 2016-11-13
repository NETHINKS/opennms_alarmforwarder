"""model of opennms_alarmforwarder
"""

from collections import OrderedDict
from sqlalchemy import create_engine
from sqlalchemy import ForeignKey, ForeignKeyConstraint, Column, Integer, String, DateTime
from sqlalchemy.types import Boolean
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import config

__config = config.Config()
engine = create_engine(__config.get_value("DatabaseConnection", "url", ""))
Session = sessionmaker(bind=engine)
Base = declarative_base()


class ActiveAlarm(Base):

    __tablename__ = "active_alarm"

    alarm_id = Column(Integer, primary_key=True)
    alarm_source = Column(String, ForeignKey("source.source_name"), primary_key=True)
    alarm_uei = Column(String)
    alarm_timestamp = Column(DateTime)
    alarm_severity = Column(String)
    alarm_node_label = Column(String)
    alarm_node_interface = Column(String)
    alarm_node_service = Column(String)
    alarm_logmsg = Column(String)
    alarm_description = Column(String)
    alarm_operinstruct = Column(String)

    parameters = relationship("ActiveAlarmParm", cascade="all, delete-orphan")
    forwarding_entries = relationship("ForwardedAlarm", cascade="all, delete-orphan")
    source = relationship("Source")

    def __str__(self):
        output = "ID: " + str(self.alarm_id)
        output += " UEI: " + self.alarm_uei
        output += " Time: " + str(self.alarm_timestamp)
        output += " Logmessage: " + self.alarm_logmsg
        return output


class ActiveAlarmParm(Base):

    __tablename__ = "active_alarm_parm"

    alarm_id = Column(Integer, primary_key=True)
    alarm_source = Column(String, primary_key=True)
    parm_name = Column(String, primary_key=True)
    parm_value = Column(String)

    __table_args__ = (ForeignKeyConstraint(["alarm_id", "alarm_source"], ["active_alarm.alarm_id", "active_alarm.alarm_source"]), {})

    alarm = relationship("ActiveAlarm")


class ForwardingRule(Base):

    __tablename__ = "forwarding_rule"

    rule_id = Column(Integer, primary_key=True)
    rule_match = Column(String)
    rule_target = Column(String, ForeignKey("target.target_name"))

    forwarding_entries = relationship("ForwardedAlarm", cascade="all, delete-orphan")
    target = relationship("Target")

    def dict_repr(self):
        data = OrderedDict([
            ("rule_id", self.rule_id),
            ("rule_match", self.rule_match),
            ("rule_target", self.rule_target)
        ])
        return data

class ForwardedAlarm(Base):

    __tablename__ = "forwarded_alarm"

    alarm_id = Column(Integer, primary_key=True)
    alarm_source = Column(String, primary_key=True)
    rule_id = Column(Integer, ForeignKey("forwarding_rule.rule_id"), primary_key=True)
    forwarded = Column(Boolean)
    forwarder_reference = Column(String)

    __table_args__ = (ForeignKeyConstraint(["alarm_id", "alarm_source"], ["active_alarm.alarm_id", "active_alarm.alarm_source"]), {})

    alarm = relationship("ActiveAlarm")
    rule = relationship("ForwardingRule")

class Target(Base):

    __tablename__ = "target"

    target_name = Column(String, primary_key=True)
    target_class = Column(String)
    target_delay = Column(Integer)
    target_parms = relationship("TargetParameter", cascade="all, delete-orphan")

    forwarding_rules = relationship("ForwardingRule", cascade="all, delete-orphan")

    def dict_repr(self):
        data = OrderedDict([
            ("target_name", self.target_name),
            ("target_class", self.target_class),
            ("target_delay", self.target_delay),
            ("target_parms", {parm.parameter_name: parm.parameter_value for parm in self.target_parms})
        ])
        return data

class TargetParameter(Base):

    __tablename__ = "target_parm"

    target_name = Column(String, ForeignKey("target.target_name"), primary_key=True)
    parameter_name = Column(String, primary_key=True)
    parameter_value = Column(String)

    target = relationship("Target")


class Source(Base):

    __tablename__ = "source"

    source_name = Column(String, primary_key=True)
    source_url = Column(String)
    source_user = Column(String)
    source_password = Column(String)
    source_filter = Column(String)
    source_status = Column(Integer)

    alarm_entries = relationship("ActiveAlarm", cascade="all, delete-orphan")

    source_status_unknown = 0
    source_status_up = 1
    source_status_down = 2

    def dict_repr(self):
        data = OrderedDict([
            ("source_name", self.source_name),
            ("source_url", self.source_url),
            ("source_user", self.source_user),
            ("source_filter", self.source_filter),
            ("source_status", self.source_status),
        ])
        return data


class LocalUser(Base):

    __tablename__ = "user"

    user_name = Column(String, primary_key=True)
    password_hash = Column(String)

    def dict_repr(self):
        data = OrderedDict([
            ("user_name", self.user_name)
        ])
        return data


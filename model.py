"""model of opennms_alarmforwarder
"""

from sqlalchemy import create_engine
from sqlalchemy import ForeignKey, ForeignKeyConstraint, Column, Integer, String, DateTime
from sqlalchemy.types import Boolean
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("postgresql://alarmforwarder:alarmforwarder@localhost/alarmforwarder")
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

    forwarding_entries = relationship("ForwardedAlarm", cascade="all, delete-orphan")
    source = relationship("Source")

    def __str__(self):
        output = "ID: " + str(self.alarm_id)
        output += " UEI: " + self.alarm_uei
        output += " Time: " + str(self.alarm_timestamp)
        output += " Logmessage: " + self.alarm_logmsg
        return output


class ForwardingRule(Base):

    __tablename__ = "forwarding_rule"

    rule_id = Column(Integer, primary_key=True)
    rule_match = Column(String)
    rule_target = Column(String, ForeignKey("target.target_name"))

    forwarding_entries = relationship("ForwardedAlarm", cascade="all, delete-orphan")
    target = relationship("Target")


class ForwardedAlarm(Base):

    __tablename__ = "forwarded_alarm"

    alarm_id = Column(Integer, primary_key=True)
    alarm_source = Column(String, primary_key=True)
    rule_id = Column(Integer, ForeignKey("forwarding_rule.rule_id"), primary_key=True)
    forwarded = Column(Boolean)

    __table_args__ = (ForeignKeyConstraint(["alarm_id", "alarm_source"], ["active_alarm.alarm_id", "active_alarm.alarm_source"]), {})

    alarm = relationship("ActiveAlarm")
    rule = relationship("ForwardingRule")


class ConfigEntry(Base):

    __tablename__ = "config"

    config_section = Column(String, primary_key=True)
    config_key = Column(String, primary_key=True)
    config_value = Column(String)


class Target(Base):

    __tablename__ = "target"

    target_name = Column(String, primary_key=True)
    target_class = Column(String)
    target_parms = relationship("TargetParameter", cascade="all, delete-orphan")

    forwarding_rules = relationship("ForwardingRule", cascade="all, delete-orphan")


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

    alarm_entries = relationship("ActiveAlarm", cascade="all, delete-orphan")

"""model of opennms_alarmforwarder
"""

from sqlalchemy import create_engine
from sqlalchemy import ForeignKey, Column, Integer, String, DateTime
from sqlalchemy.types import Boolean
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("postgresql://alarmforwarder:alarmforwarder@localhost/alarmforwarder")
Session = sessionmaker(bind=engine)
Base = declarative_base()


class ActiveAlarm(Base):

    __tablename__ = "active_alarm"

    alarm_id = Column(Integer, primary_key=True)
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


class ForwardingRule(Base):

    __tablename__ = "forwarding_rule"

    rule_id = Column(Integer, primary_key=True)
    rule_match = Column(String)
    rule_target = Column(String)
    rule_target_parm = Column(String)

    forwarding_entries = relationship("ForwardedAlarm", cascade="all, delete-orphan")


class ForwardedAlarm(Base):

    __tablename__ = "forwarded_alarm"

    alarm_id = Column(Integer, ForeignKey("active_alarm.alarm_id"), primary_key=True)
    rule_id = Column(Integer, ForeignKey("forwarding_rule.rule_id"), primary_key=True)
    forwarded = Column(Boolean)

    alarm = relationship("ActiveAlarm")
    rule = relationship("ForwardingRule")

class ConfigEntry(Base):

    __tablename__ = "config"

    config_section = Column(String, primary_key=True)
    config_key = Column(String, primary_key=True)
    config_value = Column(String)

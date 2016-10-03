"""Forwarding module for opennms_alarmforwarder"""

import sys

class Forwarder(object):

    def __init__(self, name, parameter):
        self._name = name
        self._parameter = parameter
        
    def create_forwarder(name, classname, parameter):
        classobj = getattr(sys.modules[__name__], classname)
        return classobj(name, parameter)

    def forward_alarm(self, alarm):
        pass

    def resolve_alarm(self, alarm):
        pass


class StdoutForwarder(Forwarder):

    def forward_alarm(self, alarm):
        print("Forward alarm: " + str(alarm))

    def resolve_alarm(self, alarm):
        print("Resolve alarm: " + str(alarm))

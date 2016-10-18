"""Forwarding module for opennms_alarmforwarder"""

import sys
from collections import OrderedDict

class Forwarder(object):

    default_parameters = OrderedDict()

    def __init__(self, name, parameters):
        self._name = name
        self._parameters = parameters
        
    def create_forwarder(name, classname, parameter):
        classobj = getattr(sys.modules[__name__], classname)
        return classobj(name, parameter)

    def get_default_parameters(classname):
        classobj = getattr(sys.modules[__name__], classname)
        return classobj.default_parameters

    def test_forwarder(self):
        pass

    def forward_alarm(self, alarm):
        pass

    def resolve_alarm(self, alarm):
        pass


class StdoutForwarder(Forwarder):

    default_parameters = OrderedDict([
        ("AlertMessage", "Forward alarm: %alarm_logmessage%"),
        ("ResolvedMessage", "Resolve alarm: %alarm_logmessage%")
    ])

    def test_forwarder(self):
        print("This is a test of the forwarder " + self._name)

    def forward_alarm(self, alarm):
        print("Forward alarm: " + str(alarm))

    def resolve_alarm(self, alarm):
        print("Resolve alarm: " + str(alarm))

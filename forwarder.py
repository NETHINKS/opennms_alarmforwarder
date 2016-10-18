"""Forwarding module for opennms_alarmforwarder"""

import logging
import re
import sys
from collections import OrderedDict

class Forwarder(object):

    default_parameters = OrderedDict()

    def __init__(self, name, parameters):
        self._name = name
        self._parameters = parameters
        self._logger = logging.getLogger("forwarder")
        
    def create_forwarder(name, classname, parameter):
        classobj = getattr(sys.modules[__name__], classname)
        return classobj(name, parameter)

    def get_default_parameters(classname):
        classobj = getattr(sys.modules[__name__], classname)
        return classobj.default_parameters

    def get_parameter(self, name):
        value = ""
        try:
            value = type(self).default_parameters[name]
            for parameter in self._parameters:
                if parameter.parameter_name == name:
                    value = parameter.parameter_value
        except:
            pass
        return value

    def substitute_alarm_variables(self, input_string, alarm):
        def substitute_var(match):
            replaced_var = match.group(0)
            try:
                replaced_var = str(getattr(alarm, match.group(1)))
            except:
                pass
            return replaced_var
        output = input_string
        output = re.sub("%(alarm_.*?)%", substitute_var, input_string)
        return output

    def test_forwarder(self):
        pass

    def forward_alarm(self, alarm):
        pass

    def resolve_alarm(self, alarm):
        pass


class StdoutForwarder(Forwarder):

    default_parameters = OrderedDict([
        ("AlertMessage", "Forward alarm: %alarm_timestamp% %alarm_logmsg%"),
        ("ResolvedMessage", "Resolve alarm: %alarm_timestamp% %alarm_logmsg%")
    ])

    def test_forwarder(self):
        print("This is a test of the forwarder " + self._name)

    def forward_alarm(self, alarm):
        alarm_string = self.substitute_alarm_variables(self.get_parameter("AlertMessage"), alarm)
        print(alarm_string)

    def resolve_alarm(self, alarm):
        alarm_string = self.substitute_alarm_variables(self.get_parameter("ResolvedMessage"), alarm)
        print(alarm_string)

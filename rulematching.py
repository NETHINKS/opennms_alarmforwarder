"""
Rule evaluation module

This module defines a class for rule evaluation

:license: MIT, see LICENSE for more details
:copyright: (c) 2016 by NETHINKS GmbH, see AUTORS for more details
"""
import re
import logging

class RuleEvaluator(object):
    """rule evaluation"""

    def __init__(self):
        """initialization method"""
        self.__logger = logging.getLogger("scheduler")

    def evaluate_object(self, rule, obj):
        """
        evaluates, if a rule string matches a given object.
        The matching is evaluated against the objects' fields
        """
        # split the rule in elements by character ";"
        for rule_element in filter(None, rule.split(";")):
            match = re.match("(.*?)([=~])(.*)", rule_element)
            if match:
                rule_attrib = match.group(1)
                rule_operator = match.group(2)
                rule_value = match.group(3)
                if hasattr(obj, rule_attrib):
                    if rule_operator == "=":
                        if getattr(obj, rule_attrib) != rule_value:
                            return False
                    if rule_operator == "~":
                        rulematch = re.match(rule_value, getattr(obj, rule_attrib))
                        if rulematch is None:
                            return False
                else:
                    # error_log: rule evaluation error
                    self.__logger.error("Rule evaluation error - attrib does not exist: " + rule_element)
                    return False
            else:
                # error_log: rule evaluation error
                self.__logger.error("Rule evaluation error - cannot parse rule: " + rule)
                return False
        return True

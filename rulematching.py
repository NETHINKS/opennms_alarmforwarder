"""module for evaluate rules"""

import re

class RuleEvaluator(object):

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
                    # ToDo: error_log: rule evaluation error
                    print("Rule evaluation error - attrib does not exist: " + rule_element)
                    return False
            else:
                # ToDo: error_log: rule evaluation error
                print("Rule evaluation error - cannot parse rule: " + rule)
                return False
        return True

"""Forwarding module for opennms_alarmforwarder"""

import email
from email.mime.text import MIMEText
import inspect
import json
import logging
import re
import smtplib
import sys
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from collections import OrderedDict

class Forwarder(object):

    default_parameters = OrderedDict()

    def __init__(self, name, parameters):
        self._name = name
        self._parameters = parameters
        self._logger = logging.getLogger("forwarder")

    def get_forwarder_classnames():
        classnames = []
        for class_element in Forwarder.__subclasses__():
            classnames.append(class_element.__name__)
        return classnames

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

        def substitute_parm(match):
            replaced_var = match.group(0)
            try:
                for alarm_parm in alarm.parameters:
                    if alarm_parm.parm_name == match.group(1):
                        replaced_var = alarm_parm.parm_value
            except:
                pass
            return replaced_var

        output = input_string
        output = re.sub("%(alarm_.*?)%", substitute_var, output)
        output = re.sub("%parm_(.*?)%", substitute_parm, output)
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


class SmsEagleForwarder(Forwarder):

    default_parameters = OrderedDict([
        ("url", "http://127.0.0.1/index.php/http_api/send_sms"),
        ("user", "admin"),
        ("password", "admin"),
        ("target", "+49123456789"),
        ("messageFormatAlarm", "Alarm: %alarm_logmsg%"),
        ("messageFormatResolved", "Resolved: %alarm_logmsg%")
    ])

    def test_forwarder(self):
        message = "This is a test of the forwarder " + self._name
        self.send_message(message)

    def forward_alarm(self, alarm):
        message = self.substitute_alarm_variables(self.get_parameter("messageFormatAlarm"), alarm)
        self.send_message(message)

    def resolve_alarm(self, alarm):
        message = self.substitute_alarm_variables(self.get_parameter("messageFormatResolved"), alarm)
        self.send_message(message)

    def send_message(self, message):
        # set parameters
        target = self.get_parameter("target")
        url = self.get_parameter("url")
        url_parameters = {
            "login": self.get_parameter("user"),
            "pass": self.get_parameter("password"),
            "to": target,
            "message": message
        }

        # send HTTP GET request to SMS Eagle
        try:
            requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
            response = requests.get(url, params=url_parameters)
            # check response
            if response.status_code != 200:
                self._logger.error("Could not send SMS to %s: %s", target, message)
            else:
                self._logger.info("Send SMS to %s: %s", target, message)
        except:
            self._logger.error("Could not connect to SMS Eagle")



class EmailForwarder(Forwarder):

    default_parameters = OrderedDict([
        ("smtpServer", "127.0.0.1"),
        ("smtpAuth", "true"),
        ("smtpUser", "admin"),
        ("smtpPassword", "admin"),
        ("fromAddress", "root@example.com"),
        ("target", "mail@example.com"),
        ("subjectFormatAlarm", "Alarm: %alarm_uei%"),
        ("subjectFormatResolved", "Resolved: %alarm_uei%"),
        ("messageFormatAlarm", "Alarm:\r\n %alarm_logmsg%"),
        ("messageFormatResolved", "Resolved:\r\n %alarm_logmsg%")
    ])

    def test_forwarder(self):
        subject = "Test of forwarder " + self._name
        message = "This is a test of forwarder " + self._name
        self.send_message(subject, message)

    def forward_alarm(self, alarm):
        subject = self.substitute_alarm_variables(self.get_parameter("subjectFormatAlarm"), alarm)
        message = self.substitute_alarm_variables(self.get_parameter("messageFormatAlarm"), alarm)
        self.send_message(subject, message)

    def resolve_alarm(self, alarm):
        subject = self.substitute_alarm_variables(self.get_parameter("subjectFormatResolved"), alarm)
        message = self.substitute_alarm_variables(self.get_parameter("messageFormatResolved"), alarm)
        self.send_message(subject, message)

    def send_message(self, subject, message):
        # set parameters
        from_address = self.get_parameter("fromAddress")
        to_address = self.get_parameter("target")
        smtp_host = self.get_parameter("smtpServer")
        smtp_user = self.get_parameter("smtpUser")
        smtp_password = self.get_parameter("smtpPassword")
        smtp_auth = False
        if self.get_parameter("smtpAuth") == "true":
            smtp_auth = True

        # create message
        message_object = MIMEText(message)
        message_object["Subject"] = subject
        message_object["From"] = from_address
        message_object["To"] = to_address

        # send mail
        try:
            with smtplib.SMTP() as smtp_connection:
                smtp_connection.connect(smtp_host)
                if smtp_auth:
                    smtp_connection.login(smtp_user, smtp_password)
                smtp_connection.send_message(message_object)
                smtp_connection.quit()
            self._logger.info("Send mail to %s: subject: %s", to_address, subject)
        except:
            self._logger.error("Could not send mail to %s: subject: %s", to_address, message)

class OtrsTicketForwarder(Forwarder):

    default_parameters = OrderedDict([
        ("otrsRestUrl", "http://localhost/otrs/nph-genericinterface.pl/Webservice/OpenNMS"),
        ("otrsRestUser", "admin"),
        ("otrsRestPassword", "admin"),
        ("otrsQueue", "Raw"),
        ("otrsCustomerMail", "test@example.com"),
        ("subjectFormatAlarm", "Alarm: %alarm_uei%"),
        ("subjectFormatResolved", "Resolved: %alarm_uei%"),
        ("messageFormatAlarm", "Alarm:\r\n %alarm_logmsg%"),
        ("messageFormatResolved", "The alarm was resolved.")
    ])

    def test_forwarder(self):
        subject = "Test of opennms_alarmforwarder"
        message = "This is a test of opennms_alarmforwarder. You can ignore this ticket."
        self.create_ticket(subject, message)

    def forward_alarm(self, alarm):
        subject = self.substitute_alarm_variables(self.get_parameter("subjectFormatAlarm"), alarm)
        message = self.substitute_alarm_variables(self.get_parameter("messageFormatAlarm"), alarm)
        self.create_ticket(subject, message)

    def resolve_alarm(self, alarm):
        pass

    def create_ticket(self, subject, message):
        result_ticketno = "0"
        url = self.get_parameter("otrsRestUrl")
        user = self.get_parameter("otrsRestUser")
        password = self.get_parameter("otrsRestPassword")
        queue = self.get_parameter("otrsQueue")

        request_url = "%s/TicketCreate?UserLogin=%s&Password=%s" % (url, user, password)
        request_headers = {
            "Content-Type": "application/json"
        }
        request_data = {}
        request_data["Ticket"] = {}
        request_data["Ticket"]["Title"] = subject
        request_data["Ticket"]["Type"] = "Incident"
        request_data["Ticket"]["Priority"] = "3 normal"
        request_data["Ticket"]["Queue"] = "Raw"
        request_data["Ticket"]["State"] = "open"
        request_data["Ticket"]["CustomerUser"] = self.get_parameter("otrsCustomerMail")
        request_data["Article"] = {}
        request_data["Article"]["Subject"] = subject
        request_data["Article"]["Body"] = message
        request_data["Article"]["ContentType"] = "text/plain; charset=utf8"
        request_data_json = json.dumps(request_data)

        try:
            requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
            response = requests.post(request_url, data=request_data_json, headers=request_headers,
                                     verify=False)
            # check response
            if response.status_code != 200:
                self._logger.error("Could not create ticket")
            else:
                response_data = json.loads(response.text)
                try:
                    result_ticketno = response_data["TicketNumber"]
                except:
                    self._logger.error("Could not create ticket")
                self._logger.info("Ticket %s successfully created", result_ticketno)
        except:
            self._logger.error("Could not connect to OTRS")

        return result_ticketno

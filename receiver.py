"""
Receiver module

This module defines the receiver for OpenNMS alarms

:license: MIT, see LICENSE for more details
:copyright: (c) 2016 by NETHINKS GmbH, see AUTORS for more details
"""
import datetime
import logging
import xml.etree.ElementTree
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import model

class OpennmsReceiver(object):
    """Receiver for OpenNMS alarms"""

    def __init__(self, source):
        self.__source = source
        self.__logger = logging.getLogger("receiver")

    def test_connection(self):
        """tests connection to OpenNMS REST API and returns HTTP status code
        returns -1, if there was an error connecting to the server
        """
        # return code
        output = -1

        # config
        config_rest_url = self.__source.source_url
        config_rest_user = self.__source.source_user
        config_rest_pw = self.__source.source_password

        # test connection to OpenNMS REST API
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        request_url = config_rest_url + "/info"
        try:
            response = requests.get(request_url, auth=(config_rest_user, config_rest_pw),
                                    verify=False)
        except:
            return output
        return response.status_code

    def get_alarms(self):
        """Get all alarms from OpenNMS and return a map with alarm_data
        """
        alarms = {}
        parameters = {}

        # config
        config_rest_url = self.__source.source_url
        config_rest_user = self.__source.source_user
        config_rest_pw = self.__source.source_password
        config_rest_filter = self.__source.source_filter

        # get alarms from OpenNMS REST API
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        request_url = config_rest_url + "/alarms?limit=0"
        request_params = {
            "limit": 0,
            "query": config_rest_filter
        }
        try:
            response = requests.get(request_url, params=request_params, auth=(config_rest_user, config_rest_pw),
                                    verify=False)
        # error handling
        except:
            self.__logger.error("could not connect to source " + self.__source.source_name)
            raise
        if response.status_code != 200:
            error_msg = "could not connect to source " + self.__source.source_name
            error_msg += ": HTTP/" + str(response.status_code)
            self.__logger.error(error_msg)
            raise Exception(error_msg)

        # parse xml and create alarm
        xml_tree = xml.etree.ElementTree.fromstring(response.text)
        for alarm in xml_tree.findall("./alarm"):
            alarm_id = alarm.attrib["id"]
            alarm_severity = alarm.attrib["severity"]
            alarm_logmsg = None
            alarm_description = None
            alarm_uei = None
            alarm_nodelabel = None
            alarm_interface = None
            alarm_service = None
            alarm_operinstruct = None
            alarm_timestamp = None
            for logmessage in alarm.findall("./logMessage"):
                alarm_logmsg = logmessage.text
            for description in alarm.findall("./description"):
                alarm_description = description.text
            for uei in alarm.findall("./uei"):
                alarm_uei = uei.text
            for node in alarm.findall("./nodeLabel"):
                alarm_nodelabel = node.text
            for ipaddress in alarm.findall("./ipAddress"):
                alarm_interface = ipaddress.text
            for service in alarm.findall("./service"):
                alarm_service = service.text
            for operinstruct in alarm.findall("./operinstruct"):
                alarm_operinstruct = operinstruct.text
            for timestamp in alarm.findall("./firstEventTime"):
                try:
                    # parse date example 2016-08-15T15:00:03.208-04:00
                    # ignore timezone
                    alarm_timestamp = datetime.datetime.strptime(timestamp.text[:-6],
                                                                 "%Y-%m-%dT%H:%M:%S.%f")
                except:
                    # parse date example 2016-08-15T15:00:03-04:00
                    alarm_timestamp = datetime.datetime.strptime(timestamp.text[:-6],
                                                                 "%Y-%m-%dT%H:%M:%S")

            # parse alarm parameters
            alarm_parameters = []
            for parameter in alarm.findall("./parameters/parameter"):
                parm_name = parameter.attrib["name"]
                parm_value = parameter.attrib["value"]
                created_alarm_parm = model.ActiveAlarmParm(
                    alarm_id=alarm_id,
                    alarm_source=self.__source.source_name,
                    parm_name=parm_name,
                    parm_value=parm_value
                )
                alarm_parameters.append(created_alarm_parm)

            # create alarm
            created_alarm = model.ActiveAlarm(
                alarm_id=alarm_id,
                alarm_source=self.__source.source_name,
                alarm_uei=alarm_uei,
                alarm_timestamp=alarm_timestamp,
                alarm_severity=alarm_severity,
                alarm_node_label=alarm_nodelabel,
                alarm_node_interface=alarm_interface,
                alarm_node_service=alarm_service,
                alarm_logmsg=alarm_logmsg,
                alarm_description=alarm_description,
                alarm_operinstruct=alarm_operinstruct
            )
            alarms[alarm_id] = created_alarm
            parameters[alarm_id] = alarm_parameters

        # return alarm_data map
        alarm_data = {}
        alarm_data["alarms"] = alarms
        alarm_data["parameters"] = parameters
        return alarm_data

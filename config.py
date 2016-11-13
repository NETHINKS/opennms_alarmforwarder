"""Config module.
This module defines the class for getting configuration options
"""
import os
import configparser

class Config(object):
    """Class for handling configuration.
    This class handles the configuration. The configuration is
    in an ini-file. An instance of this class is used for
    getting values.
    """

    def __init__(self):
        """Creates a new config object from the config file etc/alarmforwarder.conf"""
         # get directory name
        basedir = os.path.dirname(os.path.abspath(__file__))
        self.__filename = basedir + "/etc/alarmforwarder.conf"
        self.__config = configparser.ConfigParser()
        self.__config.read(self.__filename)

    def get_value(self, section_name, key, default_value):
        """Gets a configuration value.
        This function returns the configuration value of a specific
        key within a section. If the section/key does not exist,
        the default_value will be returned.
        Args:
            section_name: name of the configuration section.
            key: key of the configuration option.
            default_value: default value.
        Returns:
            The value of the configuration option, or the default
            value, if the configuration option does not exist.
        """
        # set default value
        output = default_value

        # get value from config
        try:
            output = self.__config.get(section_name, key)
        except:
            pass

        # return value
        return output

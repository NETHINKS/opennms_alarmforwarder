"""Config module for opennms_alarmforwarder"""

import model

class Config(object):

    def __init__(self):
        pass

    def get_value(self, section, key, default=None):
        output = default
        orm_session = model.Session()
        query_config = orm_session.query(model.ConfigEntry).filter(
                                         model.ConfigEntry.config_section==section,
                                         model.ConfigEntry.config_key==key)
        try:
            output = query_config.first().config_value
        except:
            pass
        orm_session.close()
        return output

    def set_value(self, section, key, value):
        orm_session = model.Session()
        query_config = orm_session.query(model.ConfigEntry).filter(
                                         model.ConfigEntry.config_section==section,
                                         model.ConfigEntry.config_key==key)
        try:
            config_entry = query_config.first().config_value
            config_entry.value = value
        except:
            config_entry = model.ConfigEntry(
                config_section = section,
                config_key = key,
                config_value = value
            )
            orm_session.add(config_entry)
        orm_session.commit()
        orm_session.close()

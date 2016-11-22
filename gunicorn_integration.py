"""
Gunicorn support module

This module defines a wrapper for the gunicorn startup

:license: MIT, see LICENSE for more details
:copyright: (c) 2016 by NETHINKS GmbH, see AUTORS for more details
"""

import gunicorn.app.base
from gunicorn.six import iteritems

class WebApplication(gunicorn.app.base.BaseApplication):
    """Wrapper for gunicorn startup

    Args:
        - application: wsgi app
        - options: dict with gunicorn options
    """

    def __init__(self, application, options):
        """initialization method"""
        self.options = options
        self.application = application
        super(WebApplication, self).__init__()

    def load_config(self):
        """loads the configuration"""
        config = dict([(key, value) for key, value in iteritems(self.options)
                       if key in self.cfg.settings and value is not None])
        for key, value in iteritems(config):
            self.cfg.set(key.lower(), value)

    def load(self):
        """loads the application"""
        return self.application

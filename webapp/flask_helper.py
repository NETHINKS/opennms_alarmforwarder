"""
Flask helper methods

This module defines helper methods for using with Flask

:license: MIT, see LICENSE for more details
:copyright: (c) 2016 by NETHINKS GmbH, see AUTORS for more details
"""

import flask
from config import Config

def get_baseurl():
    config = Config()
    baseurl = config.get_value("Webserver", "baseurl", "")
    baseurl = baseurl.replace("%host%", flask.request.headers["Host"])
    return baseurl

def redirect(target):
    """helper method: redirect with base url if set"""
    config = Config()
    baseurl = get_baseurl()
    if baseurl is not "":
        target = baseurl + target
    return flask.redirect(target)

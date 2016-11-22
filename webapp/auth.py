"""
Webapp auth module

This module defines authentication for the webapp

:license: MIT, see LICENSE for more details
:copyright: (c) 2016 by NETHINKS GmbH, see AUTORS for more details
"""
from functools import wraps
from flask import redirect
from flask import request
from flask import session
from webapp.json_helper import json_check
from webapp.json_helper import json_result
from webapp.json_helper import json_error
import security

class AuthenticationHandler(object):
    """Class for handling authentication in Flask app"""

    @staticmethod
    def login_required(func):
        """decorator for login required
        This decorator can be used for declaring a function
        which requires authentication
        """
        @wraps(func)
        def handle_login_required(*args, **kwargs):
            # try to get username from session
            try:
                username = session["username"]
                return func(*args, **kwargs)
            except:
                pass

            # allow HTTP basic auth
            try:
                user_basic = request.authorization.username
                password_basic = request.authorization.password
                authprovider = security.AuthenticationProvider.get_authprovider()
                if authprovider.authenticate(user_basic, password_basic):
                    return func(*args, **kwargs)
            except:
                pass

            # on error: redirect to login page or return HTTP/401
            if json_check():
                return json_error("Unauthenticated", 401)
            session["redirect"] = request.full_path
            return redirect("/login")
        return handle_login_required

    @staticmethod
    def login(username, password):
        """login handling"""
        # try to authenticate the user
        authprovider = security.AuthenticationProvider.get_authprovider()
        if authprovider.authenticate(username, password):
            # set session variable
            session["username"] = username
            return True
        return False


    @staticmethod
    def logout():
        """logout handling"""
        try:
            # remove session variable
            del session["username"]
        except:
            pass

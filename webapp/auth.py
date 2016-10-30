"""auth module for webapp"""

from functools import wraps
from flask import redirect
from flask import request
from flask import session

class AuthenticationHandler(object):

    def login_required(func):
        @wraps(func)
        def handle_login_required(*args, **kwargs):
            # try to get username from session
            try:
                username = session["username"]
                return func(*args, **kwargs)
            except:
                # on error: redirect to login page
                return redirect("/login")
        return handle_login_required


    def login(username, password):
        # try to authenticate the user
        if AuthenticationHandler.authenticate(username, password):
            # set session variable
            session["username"] = username
            return True
        return False


    def logout():
        try:
            # remove session variable
            del session["username"]
        except:
            pass


    # ToDo: implementation
    def authenticate(username, password):
        if password == "admin":
            return True
        return False

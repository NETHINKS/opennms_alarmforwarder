#! /usr/bin/python3
"""
AlarmForwarder setup module

This is the setup module of AlarmForwarder. It does some
initialization before the first start

:license: MIT, see LICENSE for more details
:copyright: (c) 2016 by NETHINKS GmbH, see AUTORS for more details
"""
import binascii
import os
import config
import model
import security

def main():
    """main function"""

    print("AlarmForwarder Setup:")

    # create database structure
    print("- Creating the database structure")
    model.Base.metadata.create_all(model.engine)

    # create default user if not exists
    local_auth_provider = security.LocalUserAuthenticationProvider()
    if not local_auth_provider.list_users():
        print("- Creating default user [admin/admin]")
        local_auth_provider.create_user("admin", "admin")

    # create secret key
    print("- Creating secret key")
    local_conf = config.Config()
    secret = binascii.hexlify(os.urandom(24)).decode("utf-8")
    local_conf.set_value("Webserver", "secret", secret)

if __name__ == "__main__":
    main()

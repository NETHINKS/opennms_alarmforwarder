#! /usr/bin/python3
"""Setup module
"""

import model
import security

def main():
    print("Creating the database structure:")
    model.Base.metadata.create_all(model.engine)

    local_auth_provider = security.LocalUserAuthenticationProvider()
    if not local_auth_provider.list_users():
        print("Creating default user [admin/admin]:")
        local_auth_provider.create_user("admin", "admin")


if __name__ == "__main__":
    main()

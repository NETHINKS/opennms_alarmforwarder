"""
authentication module

This module defines authentication classes

:license: MIT, see LICENSE for more details
:copyright: (c) 2016 by NETHINKS GmbH, see AUTORS for more details
"""
import model
import config
import hashlib
import ldap3
import sys
import logging

class AuthenticationProvider(object):
    """Abstract Authentication Provider
    This class must be implemented to provide your own
    authentication methods
    """

    def __init__(self):
        """initialization method"""
        self._config = config.Config()
        self._logger = logging.getLogger("security")

    def authenticate(self, username, password):
        """authentication function
        This stub must be implemented to provide your own
        authentication method.

        Args:
            - username: username for user login
            - password: password for user login

        Returns:
            True, if authentication was successful
            False, if not.
        """
        raise NotImplementedError

    @staticmethod
    def get_authprovider():
        """Returns the configured authentication provider"""
        configuration = config.Config()
        classname = configuration.get_value("Security", "authenticationProvider",
                                            "LocalUserAuthenticationProvider")
        classobj = getattr(sys.modules[__name__], classname)
        return classobj()

class HybridLocalLdapAuthenticationProvider(AuthenticationProvider):
    """Hybrid Authentication
    Tries at first local authentication, after that, LDAP autentication
    """

    def authenticate(self, username, password):
        localAuthProvider = LocalUserAuthenticationProvider()
        ldapAuthProvider = LdapAuthenticationProvider()
        ret_value = localAuthProvider.authenticate(username, password)
        if not ret_value:
            ret_value = ldapAuthProvider.authenticate(username, password)
        return ret_value

class LocalUserAuthenticationProvider(AuthenticationProvider):
    """Authentication against a local user database"""

    def authenticate(self, username, password):
        password_hash = self.__hash_password(password)
        orm_session = model.Session()
        user = orm_session.query(model.LocalUser).\
                           filter(model.LocalUser.user_name==username).\
                           filter(model.LocalUser.password_hash==password_hash).\
                           first()
        if user is not None:
            self._logger.info("LocalUserAuthenticationProvider: Login of user %s successful", username)
            return True
        self._logger.warn("LocalUserAuthenticationProvider: Login of user %s failed", username)
        return False

    def create_user(self, username, password):
        """creates a user in local user database

        Args:
            - username: name of the user
            - password: password of the user

        Returns:
            True, if the user was created successfully
            False, if not
        """
        try:
            orm_session = model.Session()
            user = model.LocalUser(
                user_name=username,
                password_hash=self.__hash_password(password)
            )
            orm_session.add(user)
            orm_session.commit()
            orm_session.close()
        except:
            return False
        return True

    def get_user(self, username):
        """Returns the user object for the given username
        Args:
            - username: name of the user

        Returns:
            the user object or None, if the user was not found
        """
        try:
            orm_session = model.Session()
            user = orm_session.query(model.LocalUser).\
                               filter(model.LocalUser.user_name==username).\
                               first()
            orm_session.close()
        except:
            return None
        return user

    def change_password(self, username, password):
        """change password of the given user

        Args:
            - username: name of the user
            - password: new password of the user

        Returns:
            True, if password change was successful
            False, if not
        """
        try:
            orm_session = model.Session()
            user = orm_session.query(model.LocalUser).\
                               filter(model.LocalUser.user_name==username).\
                               first()
            user.password_hash = self.__hash_password(password)
            orm_session.commit()
            orm_session.close()
        except:
            return False
        return True

    def delete_user(self, username):
        """Delete the given user

        Args:
            - username: name of the user

        Returns:
            True, if the user was deleted successfully
            False, if not
        """
        orm_session = model.Session()
        user = orm_session.query(model.LocalUser).\
                           filter(model.LocalUser.user_name==username).\
                           first()
        if user is None:
            return False
        else:
            orm_session.delete(user)
            orm_session.commit()
            orm_session.close()
            return True

    def list_users(self):
        """Returns a list with all users"""
        orm_session = model.Session()
        users = orm_session.query(model.LocalUser).all()
        orm_session.close()
        return users

    def __hash_password(self, password):
        salt = "opennms_alarmforwarder"
        password_string = salt + password
        return hashlib.sha256(password_string.encode("utf-8")).hexdigest()


class LdapAuthenticationProvider(AuthenticationProvider):
    """Authentication against LDAP"""

    def authenticate(self, username, password):
        # get configuration options
        conf_url = self._config.get_value("LdapAuthentication", "url", "")
        conf_binddn = self._config.get_value("LdapAuthentication", "binddn", "")
        conf_bindpw = self._config.get_value("LdapAuthentication", "bindpassword", "")
        conf_basedn = self._config.get_value("LdapAuthentication", "basedn", "")
        conf_searchfilter = self._config.get_value("LdapAuthentication", "searchfilter", "")
        ldap_searchfilter = conf_searchfilter.replace("%username%", username)

        # connect to ldap server pool and bind
        ldap_server_urls = filter(None, conf_url.split(";"))
        ldap_server_pool = []
        for ldap_server_url in ldap_server_urls:
            ldap_server_pool.append(ldap3.Server(ldap_server_url))
        try:
            ldap_connection = ldap3.Connection(ldap_server_pool, conf_binddn, conf_bindpw, auto_bind=True)
        except Exception as e:
            self._logger.error("LdapAuthenticationProvider: Failed to connect to LDAP server %s. Exception: %s",
                               ldap_server_pool, e)
            ldap_connection = False
        if ldap_connection is False:
            return False
        self._logger.debug("LdapAuthenticationProvider: Connect to LDAP server %s successful", ldap_server_pool)

        # get dn for given username and try to bind with given password
        try:
            ldap_connection.search(conf_basedn, ldap_searchfilter)
        except Exception as e:
            self._logger.error("LdapAuthenticationProvider: Failed to execute LDAP search %s. Exception: %s",
                               ldap_searchfilter, e)
            return False
        for entry in ldap_connection.entries:
            # try to bind with user dn
            try:
                try:
                    entry_dn = entry.entry_dn
                except:
                    entry_dn = entry.entry_get_dn()
                result = ldap_connection_test = ldap3.Connection(ldap_server_pool, entry_dn,
                                                                 password, auto_bind=True)
            except Exception as e:
                self._logger.debug("LdapAuthenticationProvider: Could not bind. Exception: %s", e)
                result = False
            if result:
                self._logger.info("LdapAuthenticationProvider: Login of user %s successful", username)
                return True
        self._logger.info("LdapAuthenticationProvider: Login of user %s failed", username)
        return False

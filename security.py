"""authentication module"""

import model
import hashlib

class AuthenticationProvider(object):

    def authenticate(self, username, password):
        raise ImplementationError


class LocalUserAuthenticationProvider(AuthenticationProvider):

    def authenticate(self, username, password):
        password_hash = self.__hash_password(password)
        orm_session = model.Session()
        user = orm_session.query(model.LocalUser).\
                           filter(model.LocalUser.user_name==username).\
                           filter(model.LocalUser.password_hash==password_hash).\
                           first()
        if user is not None:
            return True
        return False

    def create_user(self, username, password):
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

    def change_password(self, username, password):
        pass

    def delete_user(self, username):
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
        orm_session = model.Session()
        users = orm_session.query(model.LocalUser).all()
        orm_session.close()
        return users

    def __hash_password(self, password):
        salt = "opennms_alarmforwarder"
        password_string = salt + password
        return hashlib.sha256(password_string.encode("utf-8")).hexdigest()

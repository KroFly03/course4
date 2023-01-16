import base64
import hashlib
import hmac

from constants import PWD_HASH_SALT, PWD_HASH_ITERATIONS
from dao.models.user import User
from dao.user import UserDAO


class UserService:
    def __init__(self, dao: UserDAO):
        self.dao = dao

    def get_one(self, uid):
        return self.dao.get_one(uid)

    def create(self, data):
        data['password'] = self.get_hash(data['password'])
        user = User(**data)
        return self.dao.create(user)

    def patch(self, id, data):
        user = self.get_one(id)

        if 'name' in data:
            user.name = data.get('name')

        if 'surname' in data:
            user.surname = data.get('surname')

        return self.dao.create(user)

    def get_hash(self, password):
        hash_digest = hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS
        )

        return base64.b64encode(hash_digest)

    def get_by_email(self, username):
        return self.dao.get_by_email(username)

    def compare_passwords(self, password_hash, user_password):
        decoded_digest = base64.b64decode(password_hash)

        hash_digest = hashlib.pbkdf2_hmac(
            'sha256',
            user_password.encode('utf-8'),
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS
        )

        return hmac.compare_digest(decoded_digest, hash_digest)

    def reset_password(self, data):
        uid = data.get('id')
        password1 = data.get('password1')
        password2 = data.get('password2')

        if password1 == password2:
            password = self.get_hash(password1)
            return self.dao.reset_password(uid, password)

        raise Exception

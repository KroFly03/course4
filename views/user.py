from flask_restx import Resource, Namespace
from dao.models.user import UserSchema
from flask import request
from decorators import auth_required
from implemented import user_service


user_ns = Namespace('user')

user_schema = UserSchema()
users_schema = UserSchema(many=True)


@user_ns.route('/')
class UserView(Resource):
    @auth_required
    def get(self):
        try:
            data = request.json
            user = user_service.get_one(data.get('id'))
            return user_schema.dump(user), 200
        except Exception:
            return "Not found", 404

    @auth_required
    def patch(self):
        try:
            data = request.json
            user_service.patch(data)
            return 204
        except Exception:
            return "Not found", 404


@user_ns.route('/password')
class UserUpdatePasswordView(Resource):
    @auth_required
    def put(self):
        try:
            data = request.json
            user = user_service.reset_password(data)

            return user_schema.dump(user), 204
        except Exception as ex:
            return "Not found "+str(ex), 404

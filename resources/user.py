from ast import parse
from re import I
from models.user import UserModel
from flask_restful import Resource, reqparse

class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'username',
        type = str,
        required = True,
        help = "This field can't be blank!"
    )

    parser.add_argument(
        'password',
        type = str,
        required = True,
        help = "This field can't be blank!"
    )

    parser.add_argument(
        'role',
        type = int,
        required = True,
        help = "This field can't be blank!"
    )

    def post(self):
        data = UserRegister.parser.parse_args()

        if (UserModel.find_by_username(data['username'])):
            return {"message" : "A username with this name is already exist."}, 400

        user = UserModel(data["username"], data["password"], data["role"])
        user.save_to_db()

        return {"message" : "User created successfully."}, 201

class UserList(Resource):
    def get(self):
        users = UserModel.query.all()
        return {"users" : [user.json() for user in users]}

class User(Resource):

    @classmethod
    def get(cls, uid):
        user = UserModel.find_by_user_id(uid)

        if not user:
            return {"message" : "User not found"}, 404

        return user.json()

    @classmethod
    def delete(cls, uid):
        user = UserModel.find_by_user_id(uid)

        if not user:
            return {"message" : "User not found!"}, 404

        user.delete_from_db()
        return {"message" : "User delete successfully"}, 200
from re import U
from db import db

class UserModel(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String)
    password = db.Column(db.String)
    role = db.Column(db.Integer)

    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role

    def json(self):
        return {'uid' : self.id, 'username' : self.username, 'password' : self.password, 'role' : self.role}

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_user_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def find_by_role(cls, role):
        return cls.query.filter_by(role=role).all()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
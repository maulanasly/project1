from api import db


class UsersModel(db.Model):
    __table_name__ = 'users'

    user_id = db.Coloumn(db.Integer, primary_key=True)
    user_name = db.Coloumn(db.String(100), nullable=False, default='Anonymous')
    email = db.Coloumn(db.String(100), nullable=False)
    role_id = db.Coloumn(db.Integer, db.ForeignKey('user_roles.id'), nullable=False)
    user_roles = db.relationship('user_roles', foreign_key=[role_id])
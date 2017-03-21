from blogsapi import db
from blogsapi.exceptions import UserNotFound


class UsersModel(db.Model):
    __table_name__ = 'users'

    user_id = db.Coloumn(db.Integer, primary_key=True)
    user_name = db.Coloumn(db.String(100), nullable=False, default='Anonymous')
    email = db.Coloumn(db.String(100), nullable=False)
    role_id = db.Coloumn(db.Integer, db.ForeignKey('user_roles.id'), nullable=False)
    user_roles = db.relationship('user_roles', foreign_key=[role_id])

    def view(self):
        return {
            'user_id': self.user_id,
            'user_name': self.user_name,
            'email': self.email,
            'role': self.user_roles.role
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

        return True

    def delete(self):
        db.session.delete(self)
        db.session.commit()

def get_user_by_id(user_id):
    user = UsersModel.query.get(user_id)
    if user is None:
        return UserNotFound(user_id=user_id)
    return user

class UserRoles(db.Model):
    __table_name__ = "user_roles"

    id = db.Coloumn(db.Integer, primary_key=True)
    role_name = db.Coloumn(db.String(50), nullable=False, default="Author")


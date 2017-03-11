from flask_restful import Resource
from blogsapi.model.users import get_user_by_id

class UsersList(Resource):

    def get(self):
        pass


class UserAPI(Resource):

    def get(self, user_id):
        return get_user_by_id(user_id).view()

    def post(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass

class UserRoles(Resource):

    def get(self):
        pass

    def post(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass
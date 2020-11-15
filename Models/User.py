from flask import request
from flask_restful import Resource

# users = [
#     {
#         "name": "Hilman",
#         "age": 20
#     },
#     {
#         "name": "Dimas",
#         "age": 29
#     },
#     {
#         "name": "Rian",
#         "age": 27
#     }
# ]

users = {}


class User(Resource):

    def get(self, user_id):
        return {
            "name": users[user_id]
        }

    def put(self, user_id):
        users[user_id] = request.form["user"]
        return {"name": users[user_id]}

    def post(self):
        pass

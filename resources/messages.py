from flask import jsonify, Blueprint
from flask_restful import Resource, Api

import models


class MessageList(Resource):
    def get(self):

        result = []
        query = models.Message.select()

        for row in query:
            result.append({
                "id": row.id,
                "content": row.content,
                "published_at": row.published_at
            })

        return jsonify(result)


class MessageDetail(Resource):
    def get(self, message_id):
        return jsonify({
            "user_id": str(message_id)
        })


message_api = Blueprint("resources.messages", __name__)
api = Api(message_api)

api.add_resource(MessageList, "/api/v1/messages", endpoint="messages")
api.add_resource(MessageDetail, "/api/v1/messages/<int:message_id>")

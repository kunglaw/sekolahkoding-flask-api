from flask import Flask
# from flask_restful import Resource, Api

from resources.messages import message_api

app = Flask(__name__)
app.register_blueprint(message_api)

# api.add_resource(User, "/user")
# api.add_resource(User, "/user/<int:user_id>")
# api.add_resource(messages.MessageList, "/messages")

if __name__ == "__main__":

    app.run(debug=True)

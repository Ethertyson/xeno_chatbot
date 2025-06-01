# Created by Pritanshu on 2025-05-28

from flask import Flask
from app.routes.chat_routes import chatbot_routes

def create_app():

    app = Flask(__name__)

    #Load config from config.py
    app.config.from_object('config.Config')

    #Register Routes
    app.register_blueprint(chatbot_routes)

    return app
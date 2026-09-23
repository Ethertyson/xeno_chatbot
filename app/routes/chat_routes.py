# Created by Pritanshu on 2025-05-28

from app.utils.memory_utils import log_memory
log_memory("chat_routes.py - start")

from flask import jsonify, request, Blueprint
from app.models.chatBot import startChat
from flask import render_template

log_memory("chat_routes.py - after imports")


chatbot_routes = Blueprint('chat_routes',__name__)

@chatbot_routes.route('/')
def home():
    return render_template('index.html')


@chatbot_routes.route('/chatAiModel', methods=['POST'])
def chattingV2():
    postRequest = request.get_json()
    response = startChat.chatBotResponseByTopic(postRequest)
    return response
# -*- coding: utf-8 -*-
from flask import Flask, request
from sendler import Sendler
from settings import vk_token, vk_access_token


sendler = Sendler(vk_token)
app = Flask(__name__)


@app.route('/my_bot', methods=['POST'])
def bot():
    data = request.get_json(force=True, silent=True)
    if not data or 'type' not in data:
        return 'not ok'

    if data['type'] == 'confirmation':
        return confirmation_code
    elif data['type'] == 'message_new':
        sendler.process(data['object'])
        return 'ok'

    return 'ok' 

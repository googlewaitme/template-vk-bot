# -*- coding: utf-8 -*-
from flask import Flask, request
import vk_api
from vk_api.utils import get_random_id
from sendler import Sendler

"""
Пример бота для группы ВКонтакте использующего
callback-api для получения сообщений.
Подробнее: https://vk.com/dev/callback_api
Перед запуском необходимо установить flask (pip install flask)
Запуск:
$ FLASK_APP=callback_bot.py flask run
При развертывании запускать с помощью gunicorn (pip install gunicorn):
$ gunicorn callback_bot:app
"""

sendler = Sendler(token='2f01c7858ab3ea786cb819c16280865fe34cc392cb660c6d90af2590e13140a2e38b2c6255fd1ecdb6454')
app = Flask(__name__)
confirmation_code = '0a4cd534'

"""
При развертывании путь к боту должен быть секретный,
поэтому поменяйте my_bot на случайную строку
Например:
756630756e645f336173313372336767
Сгенерировать строку можно через:
$ python3 -c "import secrets;print(secrets.token_hex(16))"
"""
@app.route('/my_bot', methods=['POST'])
def bot():
    # получаем данные из запроса
    data = request.get_json(force=True, silent=True)
    # ВКонтакте в своих запросах всегда отправляет поле type:
    if not data or 'type' not in data:
        return 'not ok'

    # проверяем тип пришедшего события
    if data['type'] == 'confirmation':
        # если это запрос защитного кода
        # отправляем его
        return confirmation_code
    # если же это сообщение, отвечаем пользователю
    elif data['type'] == 'message_new':
        # получаем ID пользователя
        sendler.process(data['object'])
        # возвращаем серверу VK "ok" и код 200
        return 'ok'

    return 'ok'  # игнорируем другие типы
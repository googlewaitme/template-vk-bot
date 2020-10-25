from vk_api import VkApi
import random


class Sendler:
    """
    Приветствую и уважаю, 
    Этот класс нужен для отправки сообщений через vk_api
    В словарь message нужно заносить данные для отправки 
    вконктате. Процесс запуска фукнций указан в функции 
    procces. Поэтому нужно смотреть. self.obj это обьект 
    который присылает вконтакте. Можно посмотреть в 
    документации, что там есть, а можно распечатать на 
    экран. Я дарю вам этот выбор.
    С любовью, Булат Зарипов
    """
    def __init__(self, token):
        self.session = VkApi(token=token)
        self.api = self.session.get_api()

    def process(self, obj):
        self.set_object(obj)
        self.generate_answer()
        self.send_message()

    def set_object(self, obj):
        self.obj = obj

    def generate_answer(self):
        self.message = dict()
        self.message['message'] = self.make_text()
        self.message['user_id'] = self.obj['user_id']
        self.message['random_id'] = random.getrandbits(64)

    def make_text(self):
        return self.obj['body']

    def send_message(self):
        self.api.messages.send(**self.message)

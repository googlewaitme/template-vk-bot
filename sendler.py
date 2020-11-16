from vk_api import VkApi
from commands_loader import CommandsLoader 


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
        self.commands = CommandsLoader().give_commands()

    def process(self, obj):
        self.set_object(obj)
        self.generate_answer()
        self.send_message()

    def set_object(self, obj):
        self.obj = obj

    def generate_answer(self):
        for command in self.commands:
            if command.is_trigger(self.obj):
                self.message = command.create_answer_message(self.obj)
                break

    def send_message(self):
        dt = self.message.get_dict()
        self.api.messages.send(**dt)

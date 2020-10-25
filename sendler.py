from vk_api import VkApi
import random
from main import DialogFlow


class Sendler:
    def __init__(self, token):
        DIALOGFLOW_PROJECT_ID = 'small-talk-247f9'
        SESSION_ID = '81a90796dca522008b59527e4404ae8a517214c7'
        self.df = DialogFlow(DIALOGFLOW_PROJECT_ID, SESSION_ID)
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
        self.message['message'] = self.df.give_answer(self.obj['body'])
        self.message['user_id'] = self.obj['user_id']
        self.message['random_id'] = random.getrandbits(64)
        if not self.message['message']:
            self.message['message'] = 'Я тебя не понял...'

    def send_message(self):
        self.api.messages.send(**self.message)

from vk_api.keyboard import VkKeyboard
import random


class Message:
	def __init__(self, text, user_id, attachment='', keyboard=None):
		self.text = text
		self.user_id = user_id
		self.attachment = attachment
		self.random_id = random.getrandbits(64)
		if keyboard:
			self.keyboard = keyboard
		else:
			self.keyboard = VkKeyboard.get_empty_keyboard()

	def get_dict(self):
		message = dict()
		message['user_id'] = self.user_id
		message['random_id'] = self.random_id
		message['message'] = self.text
		message['keyboard'] = self.keyboard
		message['attachment'] = self.attachment
		return message



class IncommingMessage(Message):
	def __init__(self, incomming_message, longpolling=False, callback=False):
		if longpolling:
			self.make_from_longpolling(incomming_message)
		elif callback:
			self.make_from_callback(incomming_message)
		else:
			raise KeyError('Не указано откуда пришло сообщение')

	def make_from_callback(self, message):
		text = message['object']['body']
		user_id = message['object']['user_id']
		super().__init__(text, user_id)

	def make_from_longpolling(self, event):
		super().__init__(event.text, event.user_id)

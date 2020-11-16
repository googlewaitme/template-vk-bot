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

	def from_longpoll(self, obj):
		pass

	def from_callback(self, obj):
		pass

from message import Message
from keyboard.botkey import BotKeyboard


keyboard = BotKeyboard()

class Command:
	def __init__(self):
		self.triggers = ['help me']
		self.text = 'That example command'
		self.keyboard = keyboard.menu()


	def is_trigger(self, data):
		return data['body'].lower() in self.triggers


	def create_answer_message(self, data):
		message = Message(
			text=self.text, 
			user_id=data['user_id'], 
			keyboard=self.keyboard
		)
		return message

commands = [Command]

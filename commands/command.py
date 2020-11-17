from message import Message
from keyboard.botkey import BotKeyboard


keyboard = BotKeyboard()

class Command:
	def __init__(self):
		self.triggers = ['help me']
		self.text = 'That example command'
		self.keyboard = keyboard.menu()


	def is_trigger(self, incomming_message):
		return incomming_message.text.lower() in self.triggers


	def create_answer_message(self, incomming_message):
		message = Message(
			text=self.text, 
			user_id=incomming_message.user_id, 
			keyboard=self.keyboard
		)
		return message

commands = [Command]

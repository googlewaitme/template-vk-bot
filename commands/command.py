from message import Message
from keyboard.botkey import BotKeyboard


keyboard = BotKeyboard()

class Command:
	def __init__(self):
		self.triggers = ['пример триггера']
		self.text = 'Пример команды'
		self.keyboard = keyboard.menu()
		self.priority = 50


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

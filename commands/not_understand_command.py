from commands.command import *


class NotUnderstandCommand(Command):
	def __init__(self):
		super().__init__()
		self.text = 'Простите, я вас не понял'

	def is_trigger(self, message):
		return True

commands = [NotUnderstandCommand]

import importlib
import os
from commands.command import Command


class CommandsLoader:
	"""
	Данный класс подгружает все модули из нужной нам папки
	Выдергивает классы команд и возвращает их
	
	Требования: 
	
	Каждый файл-команда:
	1) должен иметь список commands, где перечислены все классы-команды без инициализации
	
	например:
	class MenuCommand(Command):
		pass
	class ShopCommand(Command):
		pass
			
	commands = [ShopCommand, MenuCommand] 
	
	Каждая папка с файлами команд:
	1) не должна иметь питоновских файлов, кроме файлов-команд
	
	Возвращает:

	Список экземпляры классов команд
	"""
	def __init__(self, commands_path='commands'):
		self.commands_path = commands_path
		self.commands = list()

	def give_commands(self):
		self.find_files()
		self.load_modules()
		self.sort_commands_by_priority()
		return self.commands

	def find_files(self):
		self.files = os.listdir("commands")

	def load_modules(self):
		self.filter_files_endswith_py()
		for file in self.files:
			print(file)
			module = self.import_module(file)
			self.check_module_for_defects(module)
			for command in module.commands:
				self.commands.append(command())
		return self.commands

	def filter_files_endswith_py(self):
		self.files = filter(lambda x: x.endswith('.py'), self.files)

	def import_module(self, filename):
		module_name = "commands." + filename[0:-3]
		module = importlib.import_module(module_name)
		return module

	def check_module_for_defects(self, module):
		assert 'commands' in dir(module), f'Module {module} hasnt commands in atrs'
		assert len(module.commands) == 1, f'Module {module} has got commands, wtih len = {len(module.commands)}'
		for command in module.commands:
			assert issubclass(command, Command) 

	def sort_commands_by_priority(self):
		self.commands = sorted(self.commands, key=lambda command: command.priority)

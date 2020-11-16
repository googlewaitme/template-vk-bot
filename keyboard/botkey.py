from keyboard.keyboard import Keyboard
from keyboard.button import Button


class BotKeyboard(Keyboard):
	def menu(self):
		about_us = Button('О нас')
		order = Button('Сделать заказ')
		information_about_enable = Button('Сделано в enable')
		catalog = Button('Каталог товаров')
		key = [[about_us], [order], [catalog], [information_about_enable]]
		return self.generate_keyboard(key)


	def catalog(self, categories_list):
		list_of_buttons = []
		for categorie in categories_list:
			list_of_buttons.append([Button(categorie)])
		list_of_buttons.append([Button('Вернуться в меню')])
		return self.generate_keyboard(list_of_buttons)

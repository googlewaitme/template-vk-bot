import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from settings import vk_token
from sendler import Sendler
from message import IncommingMessage


vk = vk_api.VkApi(token=vk_token)
longpoll = VkLongPoll(vk)
sendler = Sendler(token=vk_token)

for event in longpoll.listen():

	if event.type == VkEventType.MESSAGE_NEW:
		if event.to_me:
			message = IncommingMessage(event, longpolling=True)
			sendler.process(message)

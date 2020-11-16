import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from settings import vk_token
from sendler import Sendler


vk = vk_api.VkApi(token=vk_token)
longpoll = VkLongPoll(vk)
sendler = Sendler(token=vk_token)

for event in longpoll.listen():

	if event.type == VkEventType.MESSAGE_NEW:
		if event.to_me:
			data = dict()
			data['body'] = event.text
			data['user_id'] = event.user_id
			sendler.process(data)

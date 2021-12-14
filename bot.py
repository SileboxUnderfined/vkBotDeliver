import vk_api, math, random
from vk_api.utils import get_random_id
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor

CREDITS = """
    Бота написал: https://vk.com/vmegrikyan99
    gitHub: https://github.com/SileboxUnderfined
    Хостится с помощью heroku: https://heroku.com
    Используется библиотека vk_api: https://github.com/python273/vk_api
    Лицензия: https://github.com/SileboxUnderfined/vkBotDeliver/blob/main/LICENSE
"""

class Bot:
    def __init__(self, ownerId, albumId, token, userToken, wantCmd, receiveCmd):
        self.userToken = userToken
        self.ownerId = ownerId
        self.albumId = albumId
        self.token = token
        self.wantCmd = wantCmd
        self.receiveCmd = receiveCmd
        self.vk = vk_api.VkApi(token=self.token)
        self.longpoll = VkLongPoll(vk=self.vk, wait=25, group_id=self.ownerId)
        self.session = self.vk.get_api()
        self.userSession = vk_api.VkApi(token=self.userToken).get_api()
        self.loop()

    def loop(self):
        for event in self.longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW:
                if event.to_me:
                    msgText = event.text
                    if msgText == "Начать":
                        self.session.messages.send(ts="1",
                                                   random_id=get_random_id(),
                                                   message="Добро пожаловать! Используйте клавиатуру!",
                                                   user_id=event.user_id,
                                                   keyboard=self.createKeyboard())
                    if msgText == "О боте":
                        self.session.messages.send(ts="1",
                                                   random_id=get_random_id(),
                                                   message=CREDITS,
                                                   user_id=event.user_id,
                                                   keyboard=self.createKeyboard())

                    if msgText == self.wantCmd:
                        attach = self.randomSelector()
                        self.session.messages.send(ts="1",
                                                   random_id=get_random_id(),
                                                   message=self.receiveCmd,
                                                   user_id=event.user_id,
                                                   keyboard=self.createKeyboard(),
                                                   attachment=attach)

    def randomSelector(self):
        """album = self.userSession.photos.getAlbums(owner_id=-self.ownerId,album_ids=self.albumId)
        photosCount = album['items'][0]['size']
        count = int(math.modf(photosCount/1000)[1])
        photos = list()"""
        r = self.userSession.photos.get(owner_id=-self.ownerId,
                                        album_id=self.albumId,
                                        count=1000)

        photos = r['items']
        """for i in range(count+1):
            r = self.userSession.photos.get(owner_id=-self.ownerId,
                                        album_id=self.albumId,
                                        count=1000)

            photos += r['items']"""

        randomed = random.choice(photos)
        result = f'photo{randomed["owner_id"]}_{randomed["id"]}'
        return result

    def createKeyboard(self):
        keyboard = VkKeyboard()
        keyboard.add_button(self.wantCmd, color=VkKeyboardColor.POSITIVE)
        keyboard.add_line()
        keyboard.add_button("""О боте""", color=VkKeyboardColor.SECONDARY)
        return keyboard.get_keyboard()
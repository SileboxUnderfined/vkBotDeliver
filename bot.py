import vk_api, math, random
from flask import Flask, request
from vk_api.utils import get_random_id
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor

CREDITS = """
    Бота написал: https://vk.com/vmegrikyan99
    gitHub: https://github.com/SileboxUnderfined/vkBotDeliver/
    Хостится с помощью heroku: https://heroku.com
    Используется библиотека vk_api: https://github.com/python273/vk_api
    Лицензия: https://github.com/SileboxUnderfined/vkBotDeliver/blob/main/LICENSE
"""

class Bot:
    def __init__(self, ownerId, albumId, token, userPhone, userPassword, wantCmd, receiveCmd, callbackServer=0, secretCode=""):
        self.userPhone = userPhone
        self.userPassword = userPassword
        self.ownerId = ownerId
        self.albumId = albumId
        self.token = token
        self.wantCmd = wantCmd
        self.receiveCmd = receiveCmd
        self.vk = vk_api.VkApi(token=self.token)
        if callbackServer == 0:
            self.longpoll = VkLongPoll(vk=self.vk, wait=25, group_id=self.ownerId)
        else:
            self.server = Flask(__name__)
            self.confirmCode = secretCode
        self.session = self.vk.get_api()
        self.userVkApi = vk_api.VkApi(login=self.userPhone,password=self.userPassword,auth_handler=self.authHandler)
        self.userVkApi.auth()
        self.userSession = self.userVkApi.get_api()
        if callbackServer == 0:
            self.loop()
        else:
            self.callbackLoop()
            self.server.add_url_rule("/",methods=['POST'])

    def callbackLoop(self):
        data = request.get_json(force=True,silent=True)
        if not data or 'type' not in data:
            return 'not ok'

        if data['type'] == 'confirmation':
            return self.confirmCode

        elif data['type'] == 'message_new':
            userId = data['object']['from_id']
            msgText = data['object']['text']
            self.session.messages.send(ts="1",
                                       random_id=get_random_id(),
                                       message="Добро пожаловать! Используйте клавиатуру!",
                                       user_id=event.user_id,
                                       keyboard=self.createKeyboard())

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

    def authHandler(self):
        print("Ниже введите код двухфакторной аутентификации: ")
        code = input(">>> ")
        remember_device = True
        return code, remember_device
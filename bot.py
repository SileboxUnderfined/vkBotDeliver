import vk_api
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
    def __init__(self, albumId, token, wantCmd, receiveCmd):
        self.albumId = albumId
        self.token = token
        self.wantCmd = wantCmd
        self.receiveCmd = receiveCmd
        self.vk = vk_api.VkApi(token=self.token)
        self.longpoll = VkLongPoll(self.vk)
        self.session = self.vk.get_api()
        self.loop()

    def loop(self):
        for event in self.longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW:
                if event.to_me:
                    msgText = event.text
                    print(dir(event))
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
        pass

    def createKeyboard(self):
        keyboard = VkKeyboard()
        keyboard.add_button(self.wantCmd, color=VkKeyboardColor.POSITIVE)
        keyboard.add_line()
        keyboard.add_button("""О боте""", color=VkKeyboardColor.SECONDARY)
        return keyboard.get_keyboard()
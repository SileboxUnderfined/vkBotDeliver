import os
from vk_api.keyboard import VkKeyboard, VkKeyboardColor

CREDITS = """
    Бота написал: https://vk.com/vmegrikyan99
    gitHub: https://github.com/SileboxUnderfined/vkBotDeliver/
    Хостится с помощью heroku: https://heroku.com
    Используется библиотека vk_api: https://github.com/python273/vk_api
    Лицензия: https://github.com/SileboxUnderfined/vkBotDeliver/blob/main/LICENSE
"""

"""def authHandler(bs, userId):
    bs.messages.send(user_id=userId,message="Введи код двухфакторки")
    key = input(">>> ")
    rememberDevice = True
    return key, rememberDevice"""

def getKeyboard():
    keyboard = VkKeyboard()
    keyboard.add_button(os.environ['WANT_CMD'],color=VkKeyboardColor.POSITIVE)
    keyboard.add_line()
    keyboard.add_button("О боте", color=VkKeyboardColor.SECONDARY)
    return keyboard.get_keyboard()
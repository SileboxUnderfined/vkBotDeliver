import os, random, requests, json
from vk_api.keyboard import VkKeyboard, VkKeyboardColor


CREDITS = """
    Бота написал: https://vk.com/vmegrikyan99
    gitHub: https://github.com/SileboxUnderfined/vkBotDeliver/
    Хостится с помощью heroku: https://heroku.com
    Используется библиотека vk_api: https://github.com/python273/vk_api
    Лицензия: https://github.com/SileboxUnderfined/vkBotDeliver/blob/main/LICENSE
"""

def loadPhotos():
    url = f'https://api.jsonbin.io/v3/b/{os.environ["JSONBIN_ID"]}/latest'
    headers = {
        'X-Master-Key':os.environ['JSONBIN_KEY']
    }
    req = requests.get(url, json=None, headers=headers)
    unjsoned = json.loads(req.text)
    photos = unjsoned["record"]["photos"]
    return photos

photos = list()

def randomSelector(photos):
    result = random.choice(photos)
    return result

def getKeyboard():
    keyboard = VkKeyboard()
    keyboard.add_button(os.environ['WANT_CMD'],color=VkKeyboardColor.POSITIVE)
    keyboard.add_line()
    keyboard.add_button("О боте", color=VkKeyboardColor.SECONDARY)
    return keyboard.get_keyboard()

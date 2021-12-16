import os, random, math, main
import vk_api.utils
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.longpoll import VkLongPoll, VkEventType
from main import bs

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

def captchaHanlder(captcha):
    userId = int(os.environ['USER_ID'])
    bs.message.send(message="Введите капчу:{}".format(captcha),user_id=userId,random_id=vk_api.utils.get_random_id())
    longpoll = VkLongPoll(bs)
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            return captcha.try_again(event.text)

def randomSelector(us):
    album = us.photos.getAlbums(owner_id=-int(os.environ['GROUP_ID']),album_ids=int(os.environ['ALBUM_ID']))
    photosCount = album['items'][0]['size']
    count = int(math.modf(photosCount/1000)[1])
    offset = int()
    photos = list()
    print(len(photos))
    for i in range(count+1):
        r = us.photos.get(owner_id=-int(os.environ['GROUP_ID']),
                          album_id=int(os.environ['ALBUM_ID']),
                          count=1000,
                          offset=offset)

        photos += r['items']
        offset += 1000

    randomed = random.choice(photos)
    result = f'photo{randomed["owner_id"]}_{randomed["id"]}'
    return result

def getKeyboard():
    keyboard = VkKeyboard()
    keyboard.add_button(os.environ['WANT_CMD'],color=VkKeyboardColor.POSITIVE)
    keyboard.add_line()
    keyboard.add_button("О боте", color=VkKeyboardColor.SECONDARY)
    return keyboard.get_keyboard()

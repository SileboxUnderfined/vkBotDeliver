# -*- coding: utf-8 -*-
from flask import Flask, request
import vk_api
from vk_api.utils import get_random_id


def authHandler():
    print("Ниже введите код двухфакторной аутентификации: ")
    code = input(">>> ")
    remember_device = True
    return code, remember_device

Data = {"token":str(),
        "userPhone":str(),
        "userPassword":str(),
        "ownerId":int(),
        "albumId":int(),
        "wantCmd":str(),
        "receiveCmd":str(),
        "secretCode":str()}

app = Flask(__name__)
bot = vk_api.VkApi(token=Data['token'])
user = vk_api.VkApi(login=Data['userPhone'],password=Data['userPassword'],auth_handler=authHandler)
user.auth()
botSession = bot.get_api()
userSession = user.get_api()

@app.route("/", methods=['POST'])
def bot():
    data = request.get_json(force=True,silent=True)
    if not data or 'type' not in data:
        return 'not ok'

    if data['type'] == 'confirmation':
        return Data['secretCode']

    elif data['type'] == 'message_new':
        fromId = data['object']['from_id']
        botSession.messages.send(message='hi',random_id=get_random_id(),user_id=fromId)
        return 'ok'

    return 'ok'

def updateData(data):
    Data['token'] = data['token']
    Data['userPhone'] = data['userPhone']
    Data['userPassword'] = data['userPassword']
    Data['ownerId'] = data['ownerId']
    Data['albumId'] = data['albumId']
    Data['wantCmd'] = data['wantCmd']
    Data['receiveCmd'] = data['receiveCmd']
    Data['secretCode'] = data['secretCode']
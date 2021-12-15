import os, vk_api, botUtils
from flask import Flask, request
from vk_api.utils import get_random_id

"""Data = {"album_id":int(os.environ['ALBUM_ID']),
        "groupId":int(os.environ['GROUP_ID']),
        "receiveCmd":os.environ['RECEIVE_CMD'],
        "wandCmd":os.environ['WANT_CMD'],
        "secretKey":os.environ['SECRET'],
        "userPhone":os.environ['USER_PHONE'],
        "userPassword":os.environ['USER_PASSWORD'],
        "token":os.environ['VK_API_KEY'],
        "confirm":os.environ['CONFIRMATION_TOKEN']}"""

app = Flask(__name__)


@app.route('/')
def index():
        return '<h1>hi!</h1>'

@app.route('/myBot', methods=['POST'])
def bot():
        data = request.get_json(force=True,silent=True)
        if not data or 'type' not in data:
                return 'not ok'

        if data['type'] == 'confirmation':
                return os.environ['confirm']

        elif data['type'] == 'message_new':
                from_id = data['object']['from_id']
                bs.messages.send(message='hi',random_id=get_random_id(),user_id=from_id)
                return 'ok'

        return 'ok'

if __name__ in "__main__":
        BotSession = vk_api.VkApi(token=os.environ['VK_API_KEY'])
        bs = BotSession.get_api()
        #userSession = vk_api.VkApi(login=os.environ['USER_PHONE'], password=os.environ['USER_PASSWORD'])
        #userSession.auth()
        #us = userSession.get_api()
        app.run(port=os.environ['PORT'],debug=False)
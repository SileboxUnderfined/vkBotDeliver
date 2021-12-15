import os, vk_api, botUtils
from flask import Flask, request
from vk_api.utils import get_random_id

app = Flask(__name__)

@app.route('/')
def index():
        return '<h1>hi!</h1>'

@app.route('/myBot', methods=['POST'])
def bot():
        data = request.get_json(force=True,silent=True)
        print(data['type'], os.environ['CONFIRMATION_TOKEN'])
        if not data or 'type' not in data:
                return 'not ok'

        if data['secret'] == os.environ['SECRET']:
                if data['type'] == 'confirmation':
                        return os.environ['CONFIRMATION_TOKEN']

                elif data['type'] == 'message_new':
                        message = data['object']['message']
                        if message['text'] == "Начать":
                                bs.messages.send(message='Используй клавиатуру!',random_id=get_random_id(),user_id=message['from_id'],keyboard=botUtils.getKeyboard())
                        return 'ok'

                return 'ok'

        return 'ok'

if __name__ in "__main__":
        BotSession = vk_api.VkApi(token=os.environ['VK_API_KEY'])
        bs = BotSession.get_api()
        userSession = vk_api.VkApi(login=os.environ['USER_PHONE'], password=os.environ['USER_PASSWORD'])
        userSession.auth()
        us = userSession.get_api()
        app.run(host="0.0.0.0",port=os.environ['PORT'],debug=False)
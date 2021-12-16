import os, vk_api, botUtils
from flask import Flask, request, render_template
from vk_api.utils import get_random_id
from vk_api.longpoll import VkLongPoll, VkEventType

app = Flask(__name__)

@app.route('/')
def index():
        return '<h1>hi!</h1>'

@app.route('/myBot', methods=['POST'])
def bot():
        data = request.get_json(force=True,silent=True)
        if not data or 'type' not in data:
                return 'not ok'

        if data['secret'] == os.environ['SECRET']:
                if data['type'] == 'confirmation':
                        return os.environ['CONFIRMATION_TOKEN']

                elif data['type'] == 'message_new':
                        message = data['object']['message']
                        if data['object']['message']['from_id'] not in users['items']:
                                bs.messages.send(message="Сначала вступи в сообщество",random_id=get_random_id(),user_id=message['from_id'])
                                return 'ok'
                        else:

                                if message['text'] == "Начать":
                                        bs.messages.send(message='Используй клавиатуру!',random_id=get_random_id(),user_id=message['from_id'],keyboard=botUtils.getKeyboard())

                                elif message['text'] == 'О боте':
                                        bs.messages.send(message=botUtils.CREDITS,random_id=get_random_id(),user_id=message['from_id'],keyboard=botUtils.getKeyboard())

                                elif message['text'] == os.environ['WANT_CMD']:
                                        attach = botUtils.randomSelector(us)
                                        bs.messages.send(message=os.environ['RECEIVE_CMD'],random_id=get_random_id(),user_id=message['from_id'],keyboard=botUtils.getKeyboard(),attachment=attach)

                                return 'ok'

                        return 'ok'

                return 'ok'

"""def captchaHandler(captcha):
        botSession = vk_api.VkApi(token=os.environ['VK_API_KEY'])
        longpoll = VkLongPoll(vk=botSession,group_id=int(os.environ['GROUP_ID']))
        bots = botSession.get_api()
        bots.messages.send(message=captcha.get_url(),random_id=get_random_id(),user_id=os.environ['USER_ID'])
        for event in longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW:
                if event.user_id == os.environ['USER_ID']:
                    return captcha.try_again(event.text)"""

if __name__ in "__main__":
        BotSession = vk_api.VkApi(token=os.environ['VK_API_KEY'])
        bs = BotSession.get_api()
        userSession = vk_api.VkApi(token=os.environ['SERVICE_KEY'], app_id=int(os.environ['APP_ID']), scope=262144)
        userSession.server_auth()
        userSession.token = {'access_token':os.environ['SERVICE_KEY'],'expires_in':0}
        us = userSession.get_api()
        users = bs.groups.getMembers(group_id=int(os.environ['GROUP_ID']))
        app.run(host="0.0.0.0",port=os.environ['PORT'],debug=False)
import os, vk_api, botUtils
from flask import Flask, request
from vk_api.utils import get_random_id

app = Flask(__name__)
photos = botUtils.loadPhotos()

@app.route('/', methods=['POST','GET'])
def index():
        if request.method == 'POST':
                if request.form.get('photosReload') == "Перезагрузить Фотографии":
                        global photos
                        photos = botUtils.loadPhotos()
                        print("reloaded photos")

                        return f"""
        <h1 color=green>Фотографии успешно обновлены!</h1>
        <h1>фотографий сейчас: {len(photos)}</h1>
        <form action="" method="POST">
          <input type="submit" value="Перезагрузить Фотографии" name="photosReload">
        </form>

        return f"""

        return """    
        <h1>фотографий сейчас: {len(photos)}</h1>
        <form action="" method="POST">
          <input type="submit" value="Перезагрузить Фотографии" name="photosReload">
        </form>
        """

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
                                        global photos
                                        attach = botUtils.randomSelector(photos)
                                        bs.messages.send(message=os.environ['RECEIVE_CMD'],random_id=get_random_id(),user_id=message['from_id'],keyboard=botUtils.getKeyboard(),attachment=attach)

                                return 'ok'

                        return 'ok'

                return 'ok'

if __name__ in "__main__":
        BotSession = vk_api.VkApi(token=os.environ['VK_API_KEY'])
        bs = BotSession.get_api()
        users = bs.groups.getMembers(group_id=int(os.environ['GROUP_ID']))
        app.run(host="0.0.0.0",port=os.environ['PORT'],debug=False)
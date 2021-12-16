import math, vk_api, json, requests

def getPhotos(us,groupId,albumId):
    album = us.photos.getAlbums(owner_id=-groupId,album_ids=albumId)
    print("Получил количество фотографий в альбоме")
    photosCount = album['items'][0]['size']
    count = int(math.modf(photosCount/1000)[1])
    offset = int()
    photos = list()
    for i in range(count+1):
        r = us.photos.get(owner_id=-groupId,
                          album_id=albumId,
                          count=1000,
                          offset=offset)

        photos += r['items']
        offset += 1000

    print("Получил фотографии в альбоме. Количество: ", len(photos))
    result = list()
    count = 0
    for photo in photos:
        r = f'photo{photo["owner_id"]}_{photo["id"]}'
        result.append(r)
        count += 1
        print(f"Преобразовал {count} фотографий")

    return result

def captchaHandler(captcha):
    print("Введите капчу: {}".format(captcha.get_url()))
    key = input()
    return captcha.try_again(key)

def createJson(photos, url, key):
    jsoned = {"count":len(photos),"photos":json.dumps(photos)}
    url = f'https://api.jsonbin.io/v3/b/{url}'
    print(key)
    print(jsoned)
    headers = {
        'Content-Type': 'application/json',
        'X-Master-Key': key
    }
    req = requests.put(url,json=jsoned,headers=headers)
    print("Загрузил фотографии на jsonbin...")
    print(req.text)

def loadData():
    f = open("settings.json",'rt')
    result = json.load(f)
    f.close()
    return result

def saveData(data):
    f = open("settings.json",'wt')
    json.dump(data,f)
    f.close()

if __name__ in "__main__":
    data = dict()
    try:
        data = loadData()
    except:
        login = input("Введите номер телефона: ")
        password = input("Введите пароль: ")
        groupId = int(input("Введите id группы(только цифры): "))
        albumId = int(input("Введите id альбома(только цифры): "))
        url = input("Введите url jsonbin: ")
        url = url.replace("https://api.jsonbin.io/b/", "")
        key = input("Введите master key jsonbin: ")
        data = {"login":login,"password":password,"groupId":groupId,"albumId":albumId,"url":url,"key":key}
        saveData(data)

    print("Вхожу в аккаунт вк...")
    user = vk_api.VkApi(login=data['login'],password=data['password'],captcha_handler=captchaHandler)
    user.auth()
    print("Вход пройден.")
    us = user.get_api()
    print("Получил доступ к API")
    photos = getPhotos(us, data['groupId'], data['albumId'])
    createJson(photos, data['url'],data['key'])
    print("Зайдите на сайт бота и перезагрузите фотографии")
    input("Нажмите Enter чтобы выйти: ")
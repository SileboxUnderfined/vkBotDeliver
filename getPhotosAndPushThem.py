import math, vk_api, json

def getPhotos(us,groupId,albumId):
    album = us.photos.getAlbums(owner_id=-groupId,album_ids=albumId)
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

    print(len(photos))
    result = list()
    for photo in photos:
        r = f'photo{photo["owner_id"]}_{photo["id"]}'
        result.append(r)

    return result

def captchaHandler(captcha):
    print("Введите капчу: {}".format(captcha.get_url()))
    key = input()
    return captcha.try_again(key)

def createJson(photos):
    f = open("photos.json",'wt')
    json.dump(photos,f)
    f.close()

if __name__ in "__main__":
    login = input("Введите номер телефона: ")
    password = input("Введите пароль: ")
    groupId = int(input("Введите id группы(только цифры): "))
    albumId = int(input("Введите id альбома(только цифры): "))
    user = vk_api.VkApi(login=login,password=password,captcha_handler=captchaHandler)
    user.auth()
    us = user.get_api()
    photos = getPhotos(us, groupId, albumId)
    createJson(photos)
    print("Загрузите photos.json на свой google disk")
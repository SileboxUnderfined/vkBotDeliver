import json, os
from bot import Bot
from boto.s3.connection import S3Connection

class Main:
    def __init__(self):
        Data = dict()
        try:
            print(S3Connection(os.environ['VK_API_KEY']))
        except:
            Data = self.jsonMethod()

        self.bot = Bot(ownerId=self.jsonData['ownerId'],albumId=self.jsonData['albumId'],token=self.jsonData['token'],userToken=self.jsonData['userToken'],wantCmd=self.jsonData['wantCmd'],receiveCmd=self.jsonData['receiveCmd'])

    def jsonMethod(self):
        self.jsonData = dict()
        if os.path.isfile("settings.json") == True:
            self.jsonData = self.loadJSON()
        else:
            print("1 - создать файл настроек")
            print("0 - загрузить файл настроек")
            choice = int(input(">> "))
            if choice == 1:
                name = input("Введите название файла(если ничего не вводить, то файл будет называться settings.json): ")
                if name == '':
                    self.jsonData = self.createJSON()
                else:
                    self.jsonData = self.createJSON(name)

            elif choice == 0:
                name = input("Введите название файла(с .json): ")
                if name == '':
                    self.jsonData = self.loadJSON()
                else:
                    self.jsonData = self.loadJSON(name)

    def loadJSON(self, name="settings.json"):
        f = open(name,'rt')
        result = json.load(f)
        print(result)
        return result

    def createJSON(self, name="settings.json"):
        ownerId = int(input("Введите id сообщества(только цифры): "))
        albumId = int(input("Введите id альбома(только цифры): "))
        token = input("Введите токен: ")
        userToken = input("Введите токен пользователя(https://vkhost.github.io/): ")
        wantCmd = input("Введите команду которая должна присылать рандомную пикчу: ")
        receiveCmd = input("Введите ответ бота на команду: ")
        data = {"ownerId":ownerId,"albumId":albumId,"token":token,"userToken":userToken,"wantCmd":wantCmd, "receiveCmd":receiveCmd}
        f = open(name,'wt')
        json.dump(data,f)
        return data

if __name__ in "__main__":
    a = Main()

import json, os
from bot import Bot

class Main:
    def __init__(self):
        Data = self.jsonMethod()
        self.bot = Bot(ownerId=Data['ownerId'],albumId=Data['albumId'],token=Data['token'],userPhone=Data['userPhone'],userPassword=Data['userPassword'],wantCmd=Data['wantCmd'],receiveCmd=Data['receiveCmd'])

    def jsonMethod(self):
        result = dict()
        if os.path.isfile("settings.json") == True:
            result = self.loadJSON()
        else:
            print("1 - создать файл настроек")
            print("0 - загрузить файл настроек")
            choice = int(input(">> "))
            if choice == 1:
                name = input("Введите название файла(если ничего не вводить, то файл будет называться settings.json): ")
                if name == '':
                    result = self.createJSON()
                else:
                    result = self.createJSON(name)

            elif choice == 0:
                name = input("Введите название файла(с .json): ")
                if name == '':
                    result = self.loadJSON()
                else:
                    result = self.loadJSON(name)

        return result

    def loadJSON(self, name="settings.json"):
        f = open(name,'rt')
        result = json.load(f)
        print(result)
        return result

    def createJSON(self, name="settings.json"):
        ownerId = int(input("Введите id сообщества(только цифры): "))
        albumId = int(input("Введите id альбома(только цифры): "))
        token = input("Введите токен: ")
        userPhone = input("Введите номер телефона пользователя, который является админом группы: ")
        userPassword = input("Введите пароль от страницы")
        wantCmd = input("Введите команду которая должна присылать рандомную пикчу: ")
        receiveCmd = input("Введите ответ бота на команду: ")
        data = {"ownerId":ownerId,"albumId":albumId,"token":token,"userPhone":userPhone,"userPassword":userPassword,"wantCmd":wantCmd, "receiveCmd":receiveCmd}
        f = open(name,'wt')
        json.dump(data,f)
        return data

if __name__ in "__main__":
    a = Main()

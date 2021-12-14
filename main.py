import json, os
from bot import Bot

class Main:
    def __init__(self):
        self.jsonData = dict()
        if os.path.isfile("settings.json") == True:
            self.loadJSON()
        else:
            print("1 - создать файл настроек")
            print("0 - загрузить файл настроек")
            choice = int(input(">> "))
            if choice == 1:
                name = input("Введите название файла(если ничего не вводить, то файл будет называться settings.json): ")
                self.jsonData = self.createJSON(name)

            elif choice == 0:
                name = input("Введите название файла(с .json): ")
                self.jsonData = self.loadJSON(name)

        self.bot = Bot(albumId=self.jsonData['albumId'],token=self.jsonData['token'],wantCmd=self.jsonData['wantCmd'],receiveCmd=self.jsonData['receiveCmd'])

    def loadJSON(self, name="settings.json"):
        f = open(name,'rt')
        result = json.load(f)
        return result

    def createJSON(self, name="settings.json"):
        albumId = int(input("Введите id альбома(только цифры): "))
        token = input("Введите токен: ")
        wantCmd = input("Введите команду которая должна присылать рандомную пикчу: ")
        receiveCmd = input("Введите ответ бота на команду: ")
        data = {"albumId":albumId,"token":token,"wantCmd":wantCmd, "receiveCmd":receiveCmd}
        f = open(name,'wt')
        json.dump(data,f)
        return data

if __name__ in "__main__":
    a = Main()

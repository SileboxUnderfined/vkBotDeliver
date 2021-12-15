def authHandler():
    print("Введите ключ двухфакторной авторизации: ")
    key = input(">>> ")
    rememberDevice = True
    return key, rememberDevice
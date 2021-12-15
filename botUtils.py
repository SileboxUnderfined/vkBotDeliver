import os
from vk_api.keyboard import VkKeyboard, VkKeyboardColor

CREDITS = """
"""

"""def authHandler(bs, userId):
    bs.messages.send(user_id=userId,message="Введи код двухфакторки")
    key = input(">>> ")
    rememberDevice = True
    return key, rememberDevice"""

def getKeyboard():
    keyboard = VkKeyboard()
    keyboard.add_button(os.environ['WANT_CMD'],color=VkKeyboardColor.POSITIVE)
    keyboard.add_line()
    keyboard.add_button("О боте", color=VkKeyboardColor.SECONDARY)
    return keyboard.get_keyboard()
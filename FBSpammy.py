import os

try:
    from SpammyGUI import *
except:
    print('It seems you dont have fbchat installed, lets fix that!')
    os.system("pip install fbchat")
    from SpammyGUI import *
    clearScreen()


user = None

while user is None:
    loginOption = startScreen()
    if loginOption == 0:
        user = loginScreen()
    else:
        user = Login(loginOption)

spammyGUI(user)

user.logout()

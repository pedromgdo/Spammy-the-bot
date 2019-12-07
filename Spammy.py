import os

try:
    from SpammyGUI import *
except:
    print('Installing dependencies...')
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

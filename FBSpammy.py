from SpammyGUI import *


startScreen()
user = loginScreen()

spammyGUI(user)

user.logout()
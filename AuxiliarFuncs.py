import os
from fbchat import Client
from fbchat.models import *

# clear the screen
def clearScreen():
    os.system('cls' if os.name=='nt' else 'clear')

def printUserList(users):
    for index in range(len(users)):
        puser = users[index]
        if (type(puser) is User):
            print("[{0}] User's name: {1}\n{friend}\n\n".format(index, puser.name, friend="This user is your friend" if puser.is_friend == True else "This user is not your friend"))
        else:
            print("[{0}] Group name: {1}\n\n".format(index, puser.name))
    choice = int(input("Choose user index:\n"))
    return users[choice]
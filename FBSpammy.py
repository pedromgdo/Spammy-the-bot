
from fbchat import Client
from fbchat.models import *
from getpass import getpass
import time
import os

#clear the screen
def clearScreen():
    os.system('cls' if os.name=='nt' else 'clear')


email = input("Email: ")
password = getpass()
#password = input('Password: ')
clearScreen()
user = Client(email,password)



def spammyGUI():
    msg = input("Message to spam: ")
    delay = int(input("Time between messages (seconds): "))
    choice = 'NULL'
    choice2 = 'NULL'

    choice = input("Do you have the destination user id? [Y/N]")

    if choice.lower() == 'y':
        cdest = input("Input destination id: ")
        dest = user.fetchThreadInfo(cdest)[cdest]

    elif choice.lower() == 'n':
        choice2 = input("[0] Check all users you've recently talked | [1] Search for name")
        if(choice2 == '0'):
            dest = printUserList(user.fetchThreadList())
        elif(choice2 == '1'):
            dest = printUserList(user.searchForUsers(input("What's the friend's name?")))


    counter = 0
    while True:
        user.send(Message(text=msg),thread_id=dest.uid,thread_type=dest.type)
        counter += 1
        print("Sent message {0} times".format(counter))
        time.sleep(delay)






def printUserList(users):
    for index in range(len(users)):
        puser = users[index]
        if (type(puser) is User):
            print("[{0}] User's name: {1} \n User's photo {2} \n User's ID: {3} \n {friend}   \n\n".format(index, puser.name,puser.photo,puser.uid, friend="This user is your friend" if puser.is_friend == True else "This user is not your friend"))
        else:
            print(" [{0}] Group name: {1} \n Group photo {2} \n Group ID: {3} \n\n".format(index,puser.name, puser.photo, puser.uid))
            print(puser)
    choice = int(input("Choose user index"))
    return users[choice]



spammyGUI()
#user.send(Message(text='Vamos League?'),thread_id=dest.uid,thread_type=ThreadType.USER)
user.logout()


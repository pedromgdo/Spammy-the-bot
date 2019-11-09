from AuxiliarFuncs import *
from getpass import getpass
import time

# Creates a Menu that returns the chosen option
def menuScreen(options):
    print("Select an Option")
    i = 0
    for var in options:
        i = i + 1
        print("[{0}] - {1}".format(str(i), var))
    choice = int(input())
    while choice < 0 or choice > len(options):
        print("Select a valid Option")
        i = 0
        for var in options:
            i = i+1
            print("[{0}] - {1}".format(str(i), var))
        choice = int(input())
    return choice


def startScreen():
    print("Welcome to Spammy the bot!")
    print("Please select an option to continue:")
    choice = menuScreen(["Login With saved Account", "Login", "Quit"])
    if choice == 1:
        print("Work in Progress")
    elif choice == 2:
        return
    elif choice == 3:
        quit()


def loginScreen():
    fail = True
    user = None
    while fail:
        email = input("Enter your Email:\n")
        password = getpass("Enter your Password:\n")
        clearScreen()
        try:
            user = Client(email, password)
            fail = False
        except:
            fail = True
            print("Error: Could not login - Username or Password incorrect.")
    return user




def spammyGUI(user):
    msg = input("Message to spam: ")
    delay = int(input("Time between messages (seconds): "))
    choice2 = 'NULL'

    choice = menuScreen(["I have the destination user ID", "I don't have the destination user ID"])
    choice = input("Do you have the destination user id? [Y/N]")

    if choice == 0:
        cdest = input("Input destination id: ")
        dest = user.fetchThreadInfo(cdest)[cdest]

    elif choice == 1:
        choice2 = menuScreen(["Check all the Users you talked with recently", "Search for a User's name"])
        if choice2 == 0:
            dest = printUserList(user.fetchThreadList())
        elif choice2 == 1:
            dest = printUserList(user.searchForUsers(input("What's the friend's name?")))

    counter = 0
    while True:
        user.send(Message(text=msg),thread_id=dest.uid,thread_type=dest.type)
        counter += 1
        print("Sent message {0} times".format(counter))
        time.sleep(delay)
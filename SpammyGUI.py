from AuxiliarFuncs import *
from getpass import getpass
import time

# Start screen for Spammy the bot!
def startScreen():
    print("Welcome to Spammy the bot!")
    success = False
    while not success:
        choice = menuScreen(["Login With saved Account", "Login", "Quit"])
        if choice == 1:
            if not hasAccountsSaved():
                print("Error: No accounts Saved")
            else:
                success = True
                clearScreen()
                print("Select an account:")
                nr = showSavedAccounts()
                choice2 = 0
                while choice2 <= 0 or choice2 > nr:  # Works since nr is always bigger than one
                    choice2 = int(input())
                    if choice2 <= 0 or choice2 > nr:
                        print("Please select a valid account")
                clearScreen()
                return choice2
        elif choice == 2:
            clearScreen()
            return 0
        elif choice == 3:
            quit()


# Lets you enter the information to try to Login without saved information
def loginScreen():
    fail, user, email, password = True, None, None, None
    while fail:
        email = input("Enter your Email ou phone number:\n")
        password = getpass("Enter your Password:\n")
        clearScreen()
        try:
            user = Client(email, password)
            fail = False
        except:
            fail = True
            print("Error: Could not login, Email/phone number or Password incorrect.")
    if not accountSaved(email):
        print("Would you like to save the login information?")
        choice = menuScreen(["Save Login Information", "Don't save Login Information"])
        if choice == 1:
            saveAccount(email, password)
    return user

# Attempts to login with saved information
def Login(savedUser):
    email = getUsername(savedUser)
    password = getPassword(savedUser)
    try:
        user = Client(email, password)
        return user
    except:
        print("Error: Could not login, Email/phone number or Password incorrect.")
        return None

# Retrieves the information to start spamming users
def spammyGUI(user):
    msg = input("Message to spam: ")
    success = False
    while not success:
        try:
            delay = int(input("Time between messages (seconds): "))
            success = True
        except:
            print("Error: Input is not a number")
    dest = None

    clearScreen()
    choice = menuScreen(["I have the destination user ID", "I don't have the destination user ID"])

    if choice == 1:
        clearScreen()
        cdest = input("Input destination id: ")
        dest = user.fetchThreadInfo(cdest)[cdest]

    elif choice == 2:
        clearScreen()
        choice2 = menuScreen(["Check all the Users you talked with recently", "Search for a User's name"])
        if choice2 == 1:
            clearScreen()
            dest = printUserList(user.fetchThreadList())
        elif choice2 == 2:
            clearScreen()
            dest = printUserList(user.searchForUsers(input("What's the friend's name?")))
    clearScreen()
    counter = 0
    while True:
        user.send(Message(text=msg), thread_id=dest.uid, thread_type=dest.type)
        counter += 1
        print("Sent message {0} times".format(counter))
        try:
            time.sleep(delay)
        except:
            return

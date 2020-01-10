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
    userL = []
    choiceF = 69

    while not success:
        try:
            delay = int(input("Time between messages (seconds): "))
            success = True
        except:
            print("Error: Input is not a number")
    dest = None
    destList = None
    cdest = ""
    while choiceF != 3:
        clearScreen()
        choice = menuScreen(["I have the destination user ID", "I don't have the destination user ID", "Append Saved ID list", "Use Saved ID list"])

        if choice == 1:
            clearScreen()
            
            cdest = input("Input destination id: (-1 to cancel)")
            if cdest != '-1':
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
        
        elif choice == 3:
            if not hasIDsaved():
                print("Error: No IDs Saved.")
            else:
                clearScreen()
                print("Select a List:")
                nr = showIDLists()
                choice2 = 0
                while choice2 <= 0 or choice2 > nr:  # Works since nr is always bigger than one
                    choice2 = int(input())
                    if choice2 <= 0 or choice2 > nr:
                        print("Please select a valid ID List")
                destList = getIDList(choice2)
                clearScreen()
        elif choice == 4:
            if not hasIDsaved():
                print("Error: No IDs Saved.")
            else:
                destList = None
                dest = None
                clearScreen()
                print("Select a List:")
                nr = showIDLists()
                choice2 = 0
                while choice2 <= 0 or choice2 > nr:  # Works since nr is always bigger than one
                    choice2 = int(input())
                    if choice2 <= 0 or choice2 > nr:
                        print("Please select a valid ID List")
                userL = getIDList(choice2)

        clearScreen()
        if cdest == '-1': continue
        if destList is not None: userL.append(destList)
        if dest is not None: userL.append(dest)
        print(printDest(userL))
        choiceF = menuScreen(["Add more friends!", "Save ID List", "Start Spamming!"])
        if choiceF == 2:
            listName = input("Input a name for the ID List: (Must be unique)")
            while hasIDListName(listName):
                clearScreen()
                print("Error: Name not unique.")
                listName = input("Input a name for the ID List: (Must be unique)")
            saveIDList(listName,userL)
    counter = 0
    while True:
        for dests in userL:
            user.send(Message(text=msg), thread_id=dests.uid, thread_type=dests.type)
        
        counter += 1
        print("Sent message {0} times".format(counter))
        
        try:
            time.sleep(delay)
        except:
            return

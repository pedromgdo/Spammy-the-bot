from helpers.AuxiliarFuncs import *
import time

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
            clearScreen()
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
                destList = getIDList(user,choice2)
                clearScreen()
        elif choice == 4:
            clearScreen()
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
                userL = getIDList(user,choice2)
                clearScreen()

        if cdest == '-1': continue
        if destList is not None: userL += destList
        if dest is not None: userL.append(dest)
        print(printDest(userL))
        choiceF = menuScreen(["Add more friends!", "Save ID List", "Start Spamming!"])
        clearScreen()
        if choiceF == 2:
            listName = input("Input a name for the ID List: (Must be unique)\n")
            while hasIDListName(listName):
                clearScreen()
                print("Error: Name not unique.")
                listName = input("Input a name for the ID List: (Must be unique)\n")
            if len(userL) != 0:
                saveIDList(listName,userL)
            else :
                clearScreen()
                print("Error: No users selected.")
    counter = 0
    if len(userL) == 0:
        print("Warning: No users selected.")
    while True:
        for dests in userL:
                user.send(Message(text=msg), thread_id=dests.uid, thread_type=dests.type)
        counter += 1
        print("Sent message {0} times".format(counter))
        
        try:
            time.sleep(delay)
        except:
            return

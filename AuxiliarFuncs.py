import os
from fbchat.models import *
from fbchat import Client
import base64
import json

path = "LoginInformation.txt"

# clear the screen
def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Creates a Menu that returns the chosen option (WIP)
def menuScreen(options):
    print("Select an Option:")
    i = 0
    for var in options:
        i = i + 1
        print("[{0}] - {1}".format(str(i), var))
    choice = int(input())
    while choice <= 0 or choice > len(options):
        print("Select a valid Option")
        i = 0
        for var in options:
            i = i+1
            print("[{0}] - {1}".format(str(i), var))
        choice = int(input())
    return choice

# Creates a Menu in which the first option is to return.
def cancellableMenu(options):
    print("Select an Option:")
    print("[{0}] - {1}".format(0,"Return"))
    i = 1
    for var in options:
        i = i + 1
        print("[{0}] - {1}".format(str(i), var))
    choice = int(input())
    while choice < 0 or choice > len(options):
        print("Select a valid Option")
        i = 0
        print("[{0}] - {1}".format(0,"Return"))
        for var in options:
            i = i+1
            print("[{0}] - {1}".format(str(i), var))
        choice = int(input())
    return choice


# Checks if there is an account saved with a certain username
def accountSaved(username):
    try:
        file = open(path, "r")
    except:
        return False
    accounts = file.readlines()
    file.close()
    for s1 in accounts:  # For every line it checks if the username is the same
        if s1.split(" ")[0] == username:
            return True
    # If it can't find it returns False
    return False

# Saves an account
def saveAccount(username, password):
    file = open(path, "a+")
    file.write(username + ' ' + b64encode(password) + '\n')
    file.close()
    return

# Checks if there are any accounts saved
def hasAccountsSaved():
    try:
        file = open(path, "r")
    except:
        return False
    accounts = file.readlines().count
    file.close()
    return accounts

# Displays all of the saved account's usernames and returns the number of accounts
def showSavedAccounts():
    file = open(path, "r")
    accounts = file.readlines()
    file.close()
    i = 1
    for ac in accounts:
        print("[{0}] - {1}".format(i, ac.split(" ")[0]))
        i = i+1
    return i-1

# Returns the [number] username
def getUsername(number):
    file = open(path, "r")
    accounts = file.readlines()
    file.close()
    for s1 in accounts:
        if number == 1:
            return s1.split(" ")[0]
        number -= 1
    return

# returns the [number] password
def getPassword(number):
    file = open(path, "r")
    accounts = file.readlines()
    file.close()
    for s1 in accounts:
        if number == 1:
            return b64decode(s1.split(" ")[1])
        number -= 1
    return

#TODO
def hasIDsaved():
    try:
        if json.loads(open('savedIDs.json')) is None:
            return False
        return True
    except:
        return False
def showIDLists():
    return
def getIDList(id):
    return

def hasIDListName(listName):
    try:
        IDLists = json.loads(open('savedIDs.json').read())
        return listName in IDLists
    except:
        return False

#TODO make work
def saveIDList(listName,userList):

    try:
        IDLists = json.loads(open('savedIDs.json').read())
    except:
        IDLists = {}
        file = open("savedIDs.json","w+")
        file.close()

    for user in userList:
        IDLists[listName].append(user.uid)

    with open("savedIDs.json", "w") as write_file:
        json.dump(IDLists, write_file)


    return


# Encode a string (password)
def b64encode(string):
  encodedBytes = base64.b64encode(string.encode("utf-8"))
  return str(encodedBytes, "utf-8")

# Decode a string (password)
def b64decode(encoded):
  return str(base64.b64decode(encoded))[2:-1]

# Prints and returns the list of users
def printUserList(users):
    for index in range(len(users)):
        puser = users[index]
        if type(puser) is User:
            print("[{0}] User's name: {1}, {friend}\n".format(index, puser.name, friend="This user is your friend" if puser.is_friend == True else "This user is not your friend"))
        else:
            print("[{0}] Group name: {1}\n".format(index, puser.name))
    choice = int(input("Choose user index:\n"))
    return users[choice]

def printDest(users):
    string = ''
    for user in users:
        string += " {0} |".format(user.name)

    return "Currently sending to: {0}".format(string[:-1])
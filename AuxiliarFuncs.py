import os
from fbchat import Client
from fbchat.models import *

path = "LoginInformation.txt"

# clear the screen
def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Creates a Menu that returns the chosen option
def menuScreen(options):
    print("Select an Option:")
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
    file.write(username + ' ' + password + '\n')
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
    file = open(path, "r+")
    accounts = file.readlines()
    file.close()
    for s1 in accounts:
        if number == 1:
            return s1.split(" ")[0]
        number -= 1
    return

# returns the [number] password
def getPassword(number):
    file = open(path, "r+")
    accounts = file.readlines()
    file.close()
    for s1 in accounts:
        if number == 1:
            return s1.split(" ")[1]
        number -= 1
    return

# Prints and returns the list of users
def printUserList(users):
    for index in range(len(users)):
        puser = users[index]
        if type(puser) is User:
            print("[{0}] User's name: {1}\n{friend}\n\n".format(index, puser.name, friend="This user is your friend" if puser.is_friend == True else "This user is not your friend"))
        else:
            print("[{0}] Group name: {1}\n\n".format(index, puser.name))
    choice = int(input("Choose user index:\n"))
    return users[choice]
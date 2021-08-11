from yaml import parse
from helpers.Configuration import load_config
import os
from SpammyGUI import *

if __name__ == '__main__':
    DEFAULT_CREDS_FILE = "credentials.yml"

    parsed_creds = load_config(DEFAULT_CREDS_FILE)
    try:
        user = Client(parsed_creds["USERNAME"],parsed_creds["PASSWORD"])
    except:
        print(f"Error: Username or Password incorrect!")
        exit()
    spammyGUI(user)

user.logout()

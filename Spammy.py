from helpers.Configuration import load_config
from fbchat import Client
from fbchat.models import *
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
    print(f"Logging out...")
    user.logout()

user.logout()

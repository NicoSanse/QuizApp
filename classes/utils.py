import json
from classes.user import User
import os

def init():
    user = User('ABC', 'ABC', 'abc@gmail.com', 'abc')
    user_dict = user.__dict__
    user_json = json.dumps(user_dict)
    
    with open('accounts.json', 'r') as f:
        if os.stat('accounts.json').st_size == 0:  
            with open('accounts.json', 'w') as f:
                        f.write('[' + user_json + ']')


def add_user(new_user_json):
      # prima di appendere il nuovo utente al file devo scrivere una virgola
                with open('accounts.json', 'r') as f:
                    content = f.read()

                content = content[:-1]
                # aggiunog una virgola
                content += ','
                #aggiungo il nuovo utente
                content += new_user_json
                # aggiungo la parentesi chiusa
                content += ']'

                with open('accounts.json', 'w') as f:
                    f.write(content)


def get_users():
    with open('accounts.json', 'r') as f:
        accounts_in_db = json.load(f)
    return accounts_in_db
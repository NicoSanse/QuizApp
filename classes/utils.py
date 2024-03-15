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


def update_user(user, score):
    with open('accounts.json', 'r') as f:
        accounts_in_db = json.load(f)

    for account in accounts_in_db:
        if account['id'] == user['id']:
            account['score'] = score

    with open('accounts.json', 'w') as f:
        json.dump(accounts_in_db, f)




def get_user_by_email(email):
    with open('accounts.json', 'r') as f:
        accounts_in_db = json.load(f)

    for account in accounts_in_db:
        if account['email'] == email:
            return account

    return None

def get_users_emails_and_passwords():
    emails_and_password = []
    with open('accounts.json', 'r') as f:
        accounts_in_db = json.load(f)

    for account in accounts_in_db:
        emails_and_password.append((account['email'], account['password']))

    return emails_and_password


def get_user_answers(request):
    question1 = request.form.get('question1')
    question2 = request.form.get('question2')
    question3 = request.form.get('question3')
    question4 = request.form.get('question4')
    question5 = request.form.get('question5')
    question6 = request.form.get('question6')
    question7 = request.form.get('question7')
    question8 = request.form.get('question8')
    question9 = request.form.get('question9')
    question10 = request.form.get('question10')

    user_answers = []
    user_answers.append(question1)
    user_answers.append(question2)
    user_answers.append(question3)
    user_answers.append(question4)
    user_answers.append(question5)
    user_answers.append(question6)
    user_answers.append(question7)
    user_answers.append(question8)
    user_answers.append(question9)
    user_answers.append(question10)

    return user_answers
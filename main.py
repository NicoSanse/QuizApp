from flask import Flask, render_template, request, redirect, url_for, session
from classes.user import User
import json
import os

app = Flask(__name__)

###### 1. Welcome page ######
@app.route('/')
def home():
    return render_template('welcome.html')


###### 2. Register page ######
@app.route('/register', methods=['GET'])
def register():
    return render_template('register.html')

@app.route('/register', methods=['POST'])
def register_post():
    nome = request.form['nome']
    cognome = request.form['cognome']
    email = request.form['email']
    password = request.form['password']
    password2 = request.form['confirmPassword']

    # creo nuovo oggetto User
    new_user = User(nome, cognome, email, password)
    # converto l'oggetto User in un dizionario
    new_user_dict = new_user.__dict__
    # converto il dizionario in un json
    new_user_json = json.dumps(new_user_dict)

    # se uno dei campi è vuoto ritorniamo un errore
    if not nome or not cognome or not email or not password or not password2:
        return render_template('register.html', error='Tutti i campi sono obbligatori')
    else:
        # controlliamo che le due password siano uguali
        if password != password2:
            return render_template('register.html', error='Le due password non corrispondono')
        else:
            # controlliamo che l'utente non esista già
            with open('accounts.json', 'r') as f:
                if os.stat('accounts.json').st_size == 0:  # se il file è vuoto
                    accounts_in_db = {}  
                else:
                    accounts_in_db = json.load(f)  
                    #accounts_in_db = json.loads(accounts_in_db)

            if new_user_json in accounts_in_db:
                return render_template('register.html', error='L\'utente esiste già')
            # inseriamo l'utente nel db
            else:
                # se il file è vuoto scrivo il json direttamente
                if len(accounts_in_db) == 0:
                    with open('accounts.json', 'w') as f:
                        json.dump(new_user_json, f)
                else:
                # altrimenti prima di appendere il nuovo utente al file devo scrivere una virgola
                # salvo il nuovo utente nel file json persistente
                    with open('accounts.json', 'a') as f:
                        # rimuovo ultimo carattere del file
                        f.seek
                        f.write(',')
                        json.dump(new_user_json, f)

    return render_template('index.html')





###### 3. Login page ######
@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login_post():
    email = request.form['email']
    password = request.form['password']
    existing_account = None

    # estraiamo l'utente dal db
    with open('accounts.json', 'r') as f:
        accounts_in_db = json.load(f)

    for account in accounts_in_db:
        if account['id']['email'] == email:
            existing_account = account
            break

    # verifichiamo l'esistenza dell'utente
    if existing_account:
        # verifichiamo la correttezza della password
        if existing_account['id']['password'] == password:
            session['user'] = existing_account
            return redirect(url_for('index'))
        # se la password è sbagliata ritorniamo un errore
        else:
            return render_template('login.html', error='Password errata')
    # se l'utente non esiste ritorniamo un errore
    else:
        return render_template('login.html', error='Utente non trovato')



####### 4. Index page ######
@app.route('/index')
def index():
    if 'user' in session:
        return render_template('index.html')
    else:
        return redirect(url_for('login'))


####### 5. Quiz page ######
@app.route('/quiz')
def quiz():
    if 'user' in session:
        return render_template('quiz.html')
    else:
        return redirect(url_for('login'))




if __name__ == '__main__':
    app.run(debug=True)

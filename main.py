from flask import Flask, render_template, request, redirect, url_for, session
from classes.user import User
from classes.utils import init, add_user, get_users
import json

app = Flask(__name__)

###### 1. Welcome page ######
@app.route('/')
def home():
    init()
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
            # controlliamo se l'utente esiste già
            if new_user_json in get_users():
                return render_template('register.html', error='L\'utente esiste già')
            # inseriamo l'utente nel db
            else:
                add_user(new_user_json)


    return redirect(url_for('index'))





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
    accounts_in_db = get_users()

    for account in accounts_in_db:
        if account['email'] == email:
            existing_account = account
            break

    # verifichiamo l'esistenza dell'utente
    if existing_account:
        # verifichiamo la correttezza della password
        if existing_account['password'] == password:
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
        return redirect(url_for('welcome'))


####### 5. Quiz page ######
@app.route('/quiz')
def quiz():
    if 'user' in session:
        return render_template('quiz.html')
    else:
        return redirect(url_for('welcome'))

@app.route('/quiz', methods=['POST'])
def quiz_post():
    # to finish
    return ''


####### 6. Logout page ######
@app.route('/logout', methods=['POST'])
def logout():
    session.pop('user', None)
    return redirect(url_for('welcome'))

####### Run app ######
if __name__ == '__main__':
    app.secret_key = 'your secret key'
    app.run(debug=True)

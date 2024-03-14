from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
from classes.user import User

app = Flask(__name__)

app.secret_key = 'your secret key'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'login'

mysql = MySQL(app)
cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)


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
    password2 = request.form['password2']

    # creo nuovo oggetto User
    new_user = User(nome, cognome, email, password)
    id = new_user.id

    # se uno dei campi è vuoto ritorniamo un errore
    if not nome or not cognome or not email or not password or not password2:
        return render_template('register.html', error='Tutti i campi sono obbligatori')
    else:
        # controlliamo che le due password siano uguali
        if password != password2:
            return render_template('register.html', error='Le due password non corrispondono')
        else:
            # controlliamo che l'utente non esista già
            cursor.execute('SELECT * FROM accounts WHERE email = %s', (email,))
            account = cursor.fetchone()
            if account:
                return render_template('register.html', error='L\'utente esiste già')
            else:
                # inseriamo l'utente nel db
                cursor.execute('INSERT INTO accounts VALUES (%s, %s, %s, %s, %s)', (id, nome, cognome, email, password))
                mysql.connection.commit()
                cursor.close()

    return render_template('index.html')





###### 3. Login page ######
@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login_post():
    # gestire controlli login e rimandare a index
    return 'ciao'










if __name__ == '__main__':
    app.run(debug=True)

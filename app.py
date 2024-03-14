from flask import Flask
from flask_mysqldb import MySQL
import MySQLdb.cursors

app = Flask(__name__)

app.secret_key = 'your secret key'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'viwuhbwfhfw'
app.config['MYSQL_DB'] = 'login'

mysql = MySQL(app)
#cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

if __name__ == '__main__':
    app.run(debug=True)

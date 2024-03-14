from app import app
from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors

@app.route('/', methods=['GET'])
def home():
    return render_template('register.html')

@app.route('/register', methods=['POST'])
def register():
    # code to register user
    #return redirect(url_for('home'))
    return 'ciao'
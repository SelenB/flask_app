from flask import Flask, request, redirect, url_for
from flask import render_template


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
    

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')

@app.route('/database')
def database():
    return render_template('database.html')
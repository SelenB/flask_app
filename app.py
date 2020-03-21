from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import forms

app = Flask(__name__)
app.secret_key = 'cs316'
app.config.from_object('config')
db = SQLAlchemy(app, session_options={'autocommit': False})

import models

@app.route('/')
def home():
    return render_template('home.html')
    

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = forms.LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/')#when we figure out hoow to connect to spotify we can redirect here.
    return render_template('login.html', form=form)
   



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
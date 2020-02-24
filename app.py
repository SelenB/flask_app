from flask import Flask, request, redirect, url_for
from flask import render_template
from database import db


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

@app.route('/select_singer')
def select_singer():
    result = db.execute("SELECT * FROM artists WHERE artist_name = 'Robyn'")
    for r in result:
        print(r)

return redirect(url_for('database'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
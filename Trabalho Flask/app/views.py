#app/template/app.py

from app.app import app

from flask import render_template


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')


@app.route('/flask')
def galeria():
    return render_template('flask.html')


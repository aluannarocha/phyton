#app/app.py

from app.app import app

from flask import render_template


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')


@app.route('/galeria')
def galeria():
    return render_template('galeria.html')


@app.route('/servicos')
def servicos():
    return render_template('servicos.html')
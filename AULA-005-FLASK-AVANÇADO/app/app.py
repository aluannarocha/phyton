# app/app.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

#configuração da base de dados (sqlte)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///loja.db'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

db = SQLAlchemy(app)
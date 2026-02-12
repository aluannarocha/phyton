# app/models.py

from app.app import app, db

# id - integer notnull pk
# nome - string not null
# descrição - string
# preço - float
# stock - integer
# imagem - string

class Produto (db.Model):

    id = db.Column (db.Integer, primary_key=True)
    nome = db.Column (db.String(100), nullable=False) 
    descricao = db.Column (db.String(500), nullable=True)
    preco = db.Column (db.Float, nullable =False)
    stock = db.Column (db.Integer,nullable=True)
    imagem = db.Column(db.String(200), default ="https://placehold.co/600x400")

    def __repr__ (self):
        return f' <Produto {self.nome}>'

# app/views.py

from app.app import app
from flask import render_template
from app.models import Produto

@app.route('/')
def index ():
    return render_template ('index.html')

@app.route('/Produtos')
def mostra_produtos():
    todos_produtos = Produto.query.all() #faz um fetchall para a variável
    return render_template('produtos.html', produtos=todos_produtos)

#adicionar rotas dinamicas


@app.route ('/produtos/<int:id_produto>')
def detalhe_produto (id_produto):
    produto_escolhido = Produto.query.get_or_404(id_produto)
    return render_template ('detalhe.html', p=produto_escolhido)


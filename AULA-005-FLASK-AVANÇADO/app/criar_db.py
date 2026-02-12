# Fazemos esta importação para ter acesso as configurações da app e da db

from app.app import app, db
from app.models import Produto

def criar_produtos_iniciais():

    # CONTEXTO DA APLICAÇÃO
    # Diz que o Flask só pode executar esse pedaço de código quando existir "contexto", 
    # ou seja, quando o servidor estiver carregado/iniciado

    with app.app_context():

        # criar fisicamente a base de dados
        db.create_all()

        # Verificação da existencia de uma query inicial
        if not Produto.query.first():
            p1 = Produto ( nome='Portátil Gmaer XPTO', descricao= 'Portátil Gamer ' 
            'incrivelmente poderoso', preco=1234.99,stock= 6, imagem = "https://placehold.co/600x400?text=Portátil+Gamer+xpto")
            p2 = Produto ( nome='Teclado Fans Fans', descricao= 'Teclado Fans Fans ' 
            'incrivelmente poderoso', preco=34.99,stock= 12, imagem = "https://placehold.co/600x400?text=Portátil+Gamer+xpto")
            p3 = Produto ( nome='Rato ratinho tatico de cs xpto', descricao= 'Rato ' 
            'incrivelmente poderoso', preco=14.99,stock= 6, imagem = "https://placehold.co/600x400?text=Portátil+Gamer+xpto")
            p4= Produto ( nome='Monitor Cilindrico xpto', descricao= 'Monitor Cilindrico xpto ' 
            'incrivelmente poderoso', preco=234.99,stock= 6, imagem = "https://placehold.co/600x400?text=Portátil+Gamer+xpto")
            p5 = Produto ( nome='Headset gillete razer xpto', descricao= ' Headset gillete razer xpto' 
            'incrivelmente poderoso', preco=14.99,stock= 12, imagem = "https://placehold.co/600x400?text=Portátil+Gamer+xpto")
            

            db.session.add_all ([p1,p2,p3,p4,p5])
            db.session.commit ()

            print ('Produtos criados!')


        else:
           print ('Base de dados já existe')
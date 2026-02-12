# run.py
from app.app import app, db
from app.views import *
from app.criar_db import criar_produtos_iniciais

if __name__ == '__main__':

    with app.app_context():
        db.create_all()

    criar_produtos_iniciais ()

    app.run(debug=True)


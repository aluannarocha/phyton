'''Crie uma base de dados chamada loja.db e
uma tabela chamada produtos com as
seguintes colunas:
id (INTEGER, PRIMARY KEY, autoincrement),
nome (TEXT),
preco (REAL),
stock (INTEGER).'''

import sqlite3

# Criar (ou ligar) à base de dados
conn = sqlite3.connect("loja.db")
cursor = conn.cursor()

# Criar a tabela produtos
cursor.execute("""
CREATE TABLE IF NOT EXISTS produtos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    preco REAL,
    stock INTEGER
)
""")

# Guardar alterações e fechar a ligação
conn.commit()
conn.close()

print("Base de dados e tabela criadas com sucesso!")
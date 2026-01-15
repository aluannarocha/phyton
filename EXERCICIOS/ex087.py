'''Insira 10 produtos fictícios na tabela
criada anteriormente. Cada produto deve
ter um nome, preço e quantidade de
stock.

Dica: Pode utilizar o executemany()'''

import sqlite3

# Conectar à base de dados
conn = sqlite3.connect("loja.db")
cursor = conn.cursor()

# Lista de produtos fictícios (nome, preco, stock)
produtos = [
    ("Camiseta", 19.99, 50),
    ("Calça Jeans", 49.90, 30),
    ("Tênis", 89.99, 20),
    ("Boné", 14.50, 40),
    ("Jaqueta", 129.90, 15),
    ("Meias", 5.99, 100),
    ("Relógio", 199.99, 10),
    ("Óculos de Sol", 79.90, 25),
    ("Mochila", 59.90, 18),
    ("Cinto", 24.99, 35)
]

# Inserir os dados
cursor.executemany(
    "INSERT INTO produtos (nome, preco, stock) VALUES (?, ?, ?)",
    produtos
)

# Guardar alterações e fechar conexão
conn.commit()
conn.close()
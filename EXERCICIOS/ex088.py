'''Altere os preços dos produtos com os ids
5, 6 e 7.'''

import sqlite3

# Conectar à base de dados
conn = sqlite3.connect("loja.db")
cursor = conn.cursor()

# Novos preços (preco, id)
novos_precos = [
    (119.90, 5),
    (6.99, 6),
    (179.99, 7)
]

# Atualizar os preços
cursor.executemany(
    "UPDATE produtos SET preco = ? WHERE id = ?",
    novos_precos
)

# Guardar alterações e fechar conexão
conn.commit()
conn.close()
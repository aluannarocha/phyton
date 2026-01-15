'''
CRIAR A BASE DE DADOS,
CRIAR A TABELA
Adicionar novos produtos (com nome, preço e
stock),
Mostrar todos os produtos da base de dados,
Alterar um produto existente (nome, preço ou
stock).'''

import sqlite3

DB_NAME = "loja.db"

def conectar():
    return sqlite3.connect(DB_NAME)

def criar_tabela():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            preco REAL,
            stock INTEGER
        )
    """)
    conn.commit()
    conn.close()

def adicionar_produto():
    nome = input("Nome do produto: ")
    preco = float(input("Preço: "))
    stock = int(input("Stock: "))

    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO produtos (nome, preco, stock) VALUES (?, ?, ?)",
        (nome, preco, stock)
    )
    conn.commit()
    conn.close()
    print("✅ Produto adicionado com sucesso!\n")

def mostrar_produtos():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM produtos")
    produtos = cursor.fetchall()
    conn.close()

    if not produtos:
        print("⚠️ Nenhum produto encontrado.\n")
        return

    print("\nID | Nome | Preço | Stock")
    print("-" * 30)
    for p in produtos:
        print(f"{p[0]} | {p[1]} | {p[2]:.2f} | {p[3]}")
    print()

def alterar_produto():
    id_produto = int(input("ID do produto a alterar: "))

    print("O que deseja alterar?")
    print("1 - Nome")
    print("2 - Preço")
    print("3 - Stock")
    opcao = input("Escolha uma opção: ")

    conn = conectar()
    cursor = conn.cursor()

    if opcao == "1":
        novo_nome = input("Novo nome: ")
        cursor.execute(
            "UPDATE produtos SET nome = ? WHERE id = ?",
            (novo_nome, id_produto)
        )
    elif opcao == "2":
        novo_preco = float(input("Novo preço: "))
        cursor.execute(
            "UPDATE produtos SET preco = ? WHERE id = ?",
            (novo_preco, id_produto)
        )
    elif opcao == "3":
        novo_stock = int(input("Novo stock: "))
        cursor.execute(
            "UPDATE produtos SET stock = ? WHERE id = ?",
            (novo_stock, id_produto)
        )
    else:
        print("❌ Opção inválida.")
        conn.close()
        return

    conn.commit()
    conn.close()
    print("✅ Produto atualizado com sucesso!\n")

def menu():
    criar_tabela()

    while True:
        print("=== Gestão de Produtos ===")
        print("1 - Adicionar produto")
        print("2 - Mostrar produtos")
        print("3 - Alterar produto")
        print("0 - Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            adicionar_produto()
        elif escolha == "2":
            mostrar_produtos()
        elif escolha == "3":
            alterar_produto()
        elif escolha == "0":
            print("👋 Programa terminado.")
            break
        else:
            print("❌ Opção inválida.\n")

if __name__ == "__main__":
    menu()


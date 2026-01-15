'''Crie um sistema que utilize o
interactive help do python. O utilizador
deve digitar o comando e o sistema deve
retornar o manual. Quando o utilizador
digitar “FIM” o programa deve encerrar.'''

def sistema_ajuda():
    while True:
        comando = input("Função ou biblioteca (FIM para sair): ").strip()

        if comando.upper() == "FIM":
            print("Encerrando o sistema de ajuda...")
            break

        print(f"\n=== AJUDA DE {comando} ===")
        help(comando)
        print("=" * 30, "\n")


# Executar o sistema
sistema_ajuda()

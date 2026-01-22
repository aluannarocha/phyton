def menu():
    while True:
        print("===== ATM MULTIBANCO =====")
        print("1 - Depositar")
        print("2 - Levantar")
        print("3 - Transferir")
        print("4 - Ver Saldo")
        print("5 - Dados da Conta")
        print("6 - Gerar Comprovativo NIB (PDF)")
        print("0 - Retirar Cartão")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            depositar()
        elif opcao == "2":
            levantar()
        elif opcao == "3":
            transferir()
        elif opcao == "4":
            ver_saldo()
        elif opcao == "5":
            dados_conta()
        elif opcao == "6":
            gerar_comprovativo_nib()
        elif opcao == "0":
            print("💳 Cartão retirado. Obrigado!")
            break
        else:
            print("❌ Opção inválida!")
if __name__ == "__main__":
    autenticar()

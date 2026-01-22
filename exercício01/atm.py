import os
from time import sleep
import stdiomask

from ..data.contas import contas_teste
from ..utils import gerar_comprovativo

class ATM:
    def __init__(self):
        self.__contas = contas_teste
        self.conta_atual = None

    
    def limpar_ecra(self):
        os.system('cls')

    
    def aguardar(self, segundos=1):
        for c in range(3):
            print('.', end='', flush=True)
            sleep(segundos)


    def autenticar(self, cartao) -> bool:
        conta = self.__contas[cartao]
        print(f'Damos as boas vindas {conta.titular}.')
        pin_input = stdiomask.getpass('Por favor, introduza o seu pin: ', mask='*')
        print('A validar', end='')

        if conta.verificar_pin(pin_input):
            self.conta_atual = conta
            return True
        else:
            return False


    def menu(self):
        while True:
            self.limpar_ecra()
            print(f'CONTA: {self.conta_atual.titular}')
            print('-----------------------------------')
            print('[ 1 ] - Levantamentos')
            print('[ 2 ] - Depositos')
            print('[ 3 ] - Consulta de Saldo')
            print('[ 4 ] - Transferencias')
            print('[ 5 ] - Dados da Conta')
            print('[ 6 ] - Obter Comprovativo NIB')
            print('[ 7 ] - Sair')
            print('-----------------------------------')

            escolha = int(input('---> '))

            if escolha == 1:
                self.menu_levantamento()
            elif escolha == 2:
                self.menu_deposito()
            elif escolha == 3:
                self.mostrar_saldo()
            elif escolha == 4:
                self.menu_transferencia()
            elif escolha == 5:
                self.mostrar_dados()
            elif escolha == 6:
                self.gerar_pdf()
            elif escolha == 7:
                print('A terminar sessão', end='')
                self.aguardar()
                self.conta_atual = None
                break
            else:
                print('Escolha inválida...')


    def iniciar(self):
        while True:
            self.limpar_ecra()
            print('==========================')
            print('        PYTHON ATM        ')
            print('==========================')
            print('\nIntroduza o cartão...')
            cartao_input = input('--> ')

            if cartao_input in self.__contas:
                if self.autenticar(cartao_input):
                    self.aguardar()
                    self.menu()
                else:
                    print('PIN INCORRETO. TENTE NOVAMENTE', end='')
                    self.aguardar()
            else:
                print('Conta inválida.', end='')
                self.aguardar()
                    

    def menu_levantamento(self):
        try:
            valor = float(input("\nValor a levantar: "))
            sucesso, msg = self.conta_atual.levantar(valor)
            print(msg)
        except ValueError:
            print("Valor inválido.")
        input("\nPressione ENTER para continuar...")

    def menu_deposito(self):
        try:
            valor = float(input("\nValor a depositar: "))
            sucesso, msg = self.conta_atual.depositar(valor)
            print(msg)
        except ValueError:
            print("Valor inválido.")
        input("\nPressione ENTER para continuar...")

    def mostrar_saldo(self):
        print(f"\nO seu saldo atual é: {self.conta_atual.saldo:.2f}€")
        # Mostrar ultimos 3 movimentos
        print("\nÚltimos movimentos:")
        for mov in self.conta_atual.historico[-3:]:
            print(mov)
        input("\nPressione ENTER para continuar...")

    def menu_transferencia(self):
        destinatario = input("\nIntroduza o nº da conta de destino: ")
        if destinatario in self.__contas and destinatario != self.conta_atual.numero_cartao:
            try:
                valor = float(input("Valor a transferir: "))
                sucesso, msg = self.conta_atual.transferir(valor, self.__contas[destinatario])
                print(msg)
            except ValueError:
                print("Valor inválido.")
        else:
            print("Conta de destino inválida ou inexistente.")
        input("\nPressione ENTER para continuar...")

    def mostrar_dados(self):
        print("\n=== DADOS DA CONTA ===")
        print(f"Titular: {self.conta_atual.titular}")
        print(f"Cartão: {self.conta_atual.numero_cartao}")
        print(f"NIB: {self.conta_atual.nib}")
        input("\nPressione ENTER para continuar...")

    def gerar_pdf(self):
        print("\nA gerar documento PDF...")
        try:
            nome_arquivo = gerar_comprovativo(self.conta_atual)
            self.aguardar()
            print(f"Sucesso! O ficheiro '{nome_arquivo}' foi criado na pasta do projeto.")
        except Exception as e:
            print(f"Erro ao gerar PDF: {e}")
        input("\nPressione ENTER para continuar...")
# Como crio uma class?
class ATM:
    def __init__(self, conta):
        self.conta = conta
        self.acesso = False

    def depositar(self):
        valor_depositar = float(input('Valor a depositar: '))
        self.conta.set_saldo(valor_depositar)
        print('Saldo atualizado')

    def levantar(self):
        valor_levantar = float(input('Valor a levantar: '))
        if valor_levantar <= self.conta.get_limite():
            self.conta.set_saldo(-valor_levantar)
            print('Levantamento efetuado com sucesso!')
            print()
        else:
            print(f'Só pode levantar até {self.conta.get_limite():.2f}€')

    def mostra_saldo(self):
        print(self.conta.get_saldo())

    def menu(self):
        while True:
            print('[ 1 ] - Levantamentos')
            print('[ 2 ] - Depósitos')
            print('[ 3 ] - Ver saldo')
            print('[ 4 ] - Sair')

            opcao = int(input('--> '))

            if opcao == 1:
                self.levantar()
            elif opcao == 2:
                self.depositar()
            elif opcao == 3:
                self.mostra_saldo()
            elif opcao == 4:
                break


class Conta:
    def __init__(self):
        self.__titular = 'Ricardo'
        self.__saldo = 500
        self.__pin = '1234'
        self.__limite = 400

    def get_titular(self):
        return self.__titular

    def get_saldo(self):
        return self.__saldo

    def set_pin(self):
        pin_antigo = input('Digite o PIN antigo: ')
        if pin_antigo == self.__pin:
            novo_pin = input('Digite o novo PIN: ')
            novo_repete = input('Digite novamente o novo PIN: ')
            if novo_pin == novo_repete:
                self.__pin = novo_pin
                print('PIN alterado com sucesso.')
            else:
                print('PIN distinto.')
        else:
            print('PIN antigo inválido.')

    def get_limite(self):
        return self.__limite

    def set_saldo(self, valor):
        self.__saldo += valor


nova_conta = Conta()
atm = ATM(nova_conta)

if __name__ == '__main__':
    atm.menu()
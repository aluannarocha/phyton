from datetime import datetime

class Conta:
    def __init__(self, titular, numero_cartao, pin, saldo, nib):
        self.__titular = titular
        self.__numero_cartao = numero_cartao
        self.__pin = pin
        self.__saldo = saldo
        self.__nib = nib
        self.__historico = []

    @property
    def titular(self):
        return self.__titular
    
    @property
    def numero_cartao(self):
        return self.__numero_cartao
    
    @property
    def nib(self):
        return self.__nib
    
    @property
    def saldo(self):
        return self.__saldo
    
    @saldo.setter
    def saldo(self, valor):
        self.__saldo += valor

    @property
    def historico(self):
        return self.__historico

    def verificar_pin(self, pin_inserido):
        return self.__pin == pin_inserido
    

    def levantar(self, valor):
        if valor > 0 and self.__saldo >= valor:
            self.__saldo -= valor
            self.registar_movimento(f'Levantamento: -{valor:.2f}€')
            return True, 'Levantamento efetuado. Retire o seu dinheiro.'
        else:
            return False, 'Saldo insuficiente ou valor inválido.'
        

    def depositar(self, valor):
        if valor > 0 and self.__saldo >= valor:
            self.__saldo += valor
            self.registar_movimento(f'Depósito: +{valor:.2f}€')
            return True, 'Depósito efetuado.'
        else:
            return False, 'Valor inválido.'
        


    def transferir(self, valor, conta_destino):
        if self.saldo >= valor and valor > 0:
            self.saldo -= valor
            conta_destino.saldo += valor
            self.registar_movimento(f"Transf. Enviada: -{valor:.2f}€ para {conta_destino.titular}")
            conta_destino.registar_movimento(f"Transf. Recebida: +{valor:.2f}€ de {self.titular}")
            return True, "Transferência realizada com sucesso."
        return False, "Saldo insuficiente."
        

    def registar_movimento(self, descricao):
        data = datetime.now().strftime('%d/%m/%Y')
        self.__historico.append(f'[{data}] {descricao}')
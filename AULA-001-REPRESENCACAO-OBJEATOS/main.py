import os

from src.entities.conta import Conta

os.system('clear')

nova_conta = Conta('Ricardo', 250000.01, 'PT50123456789', 400)

print(nova_conta)

nova_conta.obter_comprovativo()
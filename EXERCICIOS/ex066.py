




'''Crie um simulador de crédito habitação
simples e sem taxas, que solicite o nome,
ano de nascimento, rendimentos mensais,
despesas mensais, montante do crédito e
prazo em anos, guardando tudo dentro de um
dicionário. Calcule, acrescentando ao
dicionário, a idade, o remanescente após
despesas, quanto deverá pagar mensalmente
pelo crédito e se o crédito foi aprovado
sempre que o remanescente seja superior ao
valor mensal do crédito.'''
from datetime import datetime

print('---SIMULAÇÃO CRÉDITO HABITAÇÃO---')

ano_atual = datetime.now().year

dados = {}

nome_usuario = input('Digite o nome do usuário: ')
ano_nasc = int(input("Ano de nascimento: "))
rendimentos = float(input("Rendimentos mensais (€): "))
despesas = float(input("Despesas mensais (€): "))
montante = float(input("Montante do crédito (€): "))
prazo = int(input("Prazo em anos: "))

dados["nome"] = nome_usuario
dados["ano_nascimento"] = ano_nasc
dados["rendimentos"] = rendimentos
dados["despesas"] = despesas
dados["montante"] = montante
dados["prazo_anos"] = prazo

# Cálculos
dados["idade"] = ano_atual - ano_nasc
dados["remanescente"] = rendimentos - despesas

# Cálculo do valor mensal do crédito (sem taxas)
meses = prazo * 12
dados["mensalidade"] = montante / meses

# Aprovação
if dados["remanescente"] > dados["mensalidade"]:
    dados["aprovado"] = "Sim"
else:
    dados["aprovado"] = "Não"

# Mostrando o dicionário final
print("\n--- Resultados da Simulação ---")
for chave in dados:
    print(chave, ":", dados[chave])
'''Crie um programa que tenha uma função
que vai receber como parâmetro o ano de
nascimento de uma pessoa e que crie um
ficheiro que informe se a pessoa já pode
tirar a carta de condução, se precisa de
autorização do encarregado de educação
ou se não pode.

+18 anos – pode
-16 anos – não pode
-18 e +16 – com autorização'''

from datetime import date
from pathlib import Path

def verificacao(ano_nascimento):
    ano_atual = date.today().year
    idade = ano_atual - ano_nascimento

    # Determinar situação
    if idade >= 18:
        mensagem = f"Idade: {idade} anos – Pode tirar a carta de condução."
    elif idade < 16:
        mensagem = f"Idade: {idade} anos – Não pode tirar a carta de condução."
    else:  # entre 16 e 17 anos
        mensagem = f"Idade: {idade} anos – Pode apenas com autorização do encarregado de educação."

    # Criar ficheiro
    with open("resultado_carta.txt", "w", encoding="utf-8", errors='ignore') as ficheiro:
        ficheiro.write(mensagem)

    return mensagem


# Exemplo de uso:

ano = int(input('Digite o seu ano de nascimento: '))
resultado = verificacao(ano)
print(resultado)

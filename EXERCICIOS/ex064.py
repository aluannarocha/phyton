'''Crie um programa que leia o nome e a
média de um aluno, calculando a sua
situação, tudo dentro de um dicionário.
No final mostre todo o conteúdo do
dicionário.

Situação:
Média >= 9,5 – Aprovado
Média < 9,5 - Reprovado'''

aluno = {}

aluno['nome'] = input('Digite o nome do aluno: ')
aluno['media'] = float(input(f'Digite a media de {aluno["nome"]}: '))
aluno['situação']= 'Aprovado' if aluno['media'] >=9.5 else 'Reprovado'

print(aluno)

''' if aluno['media'] >= 9.5
        aluno['situacao'] = 'aprovado'
    else:
        aluno['situacao'] = 'reprovado'

    for chave, valor in aluno.items():
        print(f'{chave} = {valor}')'''
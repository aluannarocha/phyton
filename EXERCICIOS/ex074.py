'''Crie um programa que tenha uma função
que receba o nome de um aluno e uma
lista das suas notas. Ele deve calcular
a média do aluno e mostrar no ecrã o
nome do aluno, a sua média e se ele
ficou aprovado ou não.'''

from statistics import mean

def avaliar_aluno(nome: str, notas: list):
    media =mean(notas)
    situacao = 'Aprovado' if media>=9.5 else 'Reprovado'

    print(f'NOME: {nome}')
    print(f'MÉDIA: {media:.2f}')
    print(f'SITUAÇÃO: {situacao}')

name= 'Ricardo'
lst_notas= [9,4,5,6,7,8,9]
avaliar_aluno(name, lst_notas)

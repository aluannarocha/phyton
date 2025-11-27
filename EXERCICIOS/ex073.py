'''Crie um programa que tenha uma função
que receba vários parâmetros como
valores inteiros. O programa deve
analisar todos os valores e dizer qual
deles é o maior.'''

def maior(*valor: int):
    maior_valor = max (valor)
    print(f'O maior valor encontrado é {maior_valor}')

maior(3,2,1,1,3,5,8,9,0)
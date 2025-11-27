'''Crie um programa que tenha uma função
que receba um número inteiro e mostre a
tabuada desse número.'''

'''def tabuada ():
    numero = int(input('Digite um número inteiro: '))
    print(f'{numero} * 1 = {numero * 1}')...'''

numero = int(input("Digite um número inteiro: "))

def tabuada(n):
    print(f"Tabuada do {n}:")
    for i in range (1,11):
        print(n, 'x' ,i, '=' ,n * i)

tabuada(numero)

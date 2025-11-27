'''Crie um programa que tenha uma função
que receba vários parâmetros como
valores inteiros. O programa deve
analisar todos os valores e dizer qual
deles é o maior.'''


def maior_valor(lista):
    maior = lista[0]

    for n in lista:
        if n > maior:
            maior = n

    print("O maior valor é:", maior)

# Programa principal
numeros = [3, 8, 1, 10, 5]
maior_valor(numeros)

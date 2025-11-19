'''Crie um programa que leia uma matriz 3x3 e preencha com valores lidos pelo teclado.
No final mostre a matriz com a formatação adequada.'''

numeros = list()

[[1,2,3],[4,5,6],[7,8,9]]

for linha in range(0,3):
    temp = list()

    for coluna in range(0, 3):
        num=int(input('Digite um número: '))
        temp.append(num)

    numeros.append(temp[:])

for lista in numeros:
    for valor in lista:
        print(valor, end=' ')
    print()


'''print(numeros [0][2])
[[1,2,3],[4,5,6],[7,8,9]]
print(numeros [linha][coluna])'''


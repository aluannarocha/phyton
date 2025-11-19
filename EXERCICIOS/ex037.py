'''Faça um programa que leia um número
inteiro e diga se ele é ou não um
número primo. so pode ser dividido por 1 e ele mesmo apenas e da resto zero'''


numero=int(input('digite um número: '))
contador=0
for c in range (0,numero):
    if numero % (c+1)==0:
        contador+=1 #contador=contador+1

if contador == 2:
    print(f'o número {numero} é primo')
else:
    print(f'o número{numero} não é primo.')



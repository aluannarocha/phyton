'''Tabuada V2.0 – Faça um programa que
mostre a tabuada de vários números
inseridos pelo utilizador. O programa
deverá ser interrompido quando o
número inserido for negativo ou 0.'''

print('~*º~*º Tabuada v2.0 º*~º*~')
print('O programa é interrompido quando digita "0" ou um valor negativo.')

num = 1

while num > 0:

    num = int(input('\nDigite um número (ou 0/-negativo para sair): '))

    if num <= 0:
        print('A sair do programa...')
        break

    print(f'--- Tabuada do {num} ---')

    for c in range(1, 11):
        resultado = num * c

        print(f'{num} x {c:2} = {resultado}')
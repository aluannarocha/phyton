'''numero = int(input('Digite um número: '))

print(numero, 'x 1 =', numero * 1)
print(numero, 'x 2 =', numero * 2)
print(numero, 'x 3 =', numero * 3)
print(numero, 'x 4 =', numero * 4)
print(numero, 'x 5 =', numero * 5)
print(numero, 'x 6 =', numero * 6)
print(numero, 'x 7 =', numero * 7)
print(numero, 'x 8 =', numero * 8)
print(numero, 'x 9 =', numero * 9)
print(numero, 'x 10 =', numero * 10)'''
'''Faça um programa que mostre a tabuada
de um número introduzido pelo
utilizador.'''

numero=int(input('Digite um número: '))

for c in range(0, 10):
    print(f'{numero} x {c + 1} = {numero * (c + 1)}')
    print()

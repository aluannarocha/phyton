'''Crie um programa que gere 5 números
aleatórios dentro de um tuple. Depois
mostra a listagem de números gerados, o
menor e o maior.'''

from random import randint
minha_tuple=(randint(1,100),
             randint(1,100),
             randint(1,100),
             randint(1,100),
             randint(1,100))
print('Números gerados: ')
for numero in minha_tuple:
    print(f'\t{numero}', end='')

    if numero==minha_tuple[0]:
        menor=numero
        maior=numero
    else:
        if numero>maior:
            maior=numero
        if numero<menor:
            menor=numero

print()
print(f'o maior numero é {maior}')
print(f'o menor numero é {menor}')

'''print(max(minha_tuple))
print(min(minha_tuple))'''
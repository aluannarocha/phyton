'''Desenvolva o jogo par ou ímpar. O jogo
só será interrompido quando o jogador
perder e deverá exibir o total de
vitórias consecutivas.'''

print('~*º~*º Par ou Ímpar º*~º*~')

import random
win = 0

while True:
    num = int(input('Digite um valor entre 0 e 5: '))

    if num > 5 or num < 0:
        print('Por favor escolha um valor entre 0 e 5.')
        continue

    while True:
        num_pi = input(f'Par ou Ímpar: ').strip().lower()

        if num_pi == 'par' or num_pi == 'impar':
            break

        else:
            print('Por favor, digite "par" ou "ímpar".')
            break

    cpu = random.randint(0, 5)
    resultado = cpu + num

    if resultado % 2==0 and num_pi == 'par':
        print(f'Jogador: {num}')
        print(f'CPU: {cpu}')
        print(f'{num} + {cpu} = {resultado}')
        print('Jogador ganha')

        win+=1

    elif resultado % 2 != 0 and num_pi == 'ímpar':
        print(f'Jogador: {num}')
        print(f'CPU: {cpu}')
        print(f'{num} + {cpu} = {resultado}')
        print('Jogador ganha')

    else:
        print(f'Jogador: {num}')
        print(f'CPU: {cpu}')
        print(f'{num} + {cpu} = {resultado}')
        print('Jogador perde...')
        break

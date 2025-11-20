'''Cria um programa que crie palpites para o Euromilhões.
O programa deve perguntar quantas chaves serão geradas e
deve sortear aleatoriamente 5 números de 1 a 50(sem repetir) e 2 estrelas de 1 a 12 (sem repetir).
Cada sorteio deve ser guardado numa lista composta'''

from random import randint
from time import sleep

print('-------GERADOR DE CHAVES PARA O EUROMILHÕES------')



n_palpites=int(input('Quantos palpites deseja gerar?\n--> '))
sleep(1)
print(f'a gerar {n_palpites} palpites...\n')

for c in range (0, n_palpites):
    print(f'Palpite {c+1}')
    palpite = []
    numeros = []
    estrelas = []
    '''print(c)'''
    while len(numeros) < 5:
        numero= randint(1, 50)
        if numero not in numeros:
            numeros.append(numero)

    while len(estrelas) < 2:
        estrela= randint(1, 12)
        if estrela not in estrelas:
            estrelas.append(estrela)

    palpite.append(numeros[:])
    palpite.append(estrelas[:])

    for indice, linha in enumerate (palpite):
        print(f'indice: {indice}, linha: {linha}')
        if indice==00:
            for numero in linha:
                print(f'{numero} | ', end='')
                sleep(1)
        else:
            for estrela in linha:
                print(f'{estrela} | ', end='')
                sleep(1)

    print(palpite)


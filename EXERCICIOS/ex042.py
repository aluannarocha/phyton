'''Crie o jogo da adivinha v2.0. O
computador deve “pensar” num número de
0 a 10 e o utilizador deve adivinhar o
número escolhido. Só que agora o
jogador vai tentar adivinhar até
acertar. No final mostre quantas
tentativas foram necessárias.'''


from random import randint
from time import sleep

CPU = randint(0, 10)
tentativas=0

jogada=''
print(CPU)
print('---- JOGO DA ADIVINHA V2.0 ----')
sleep(1)
print(' Pensei em um número entre 0 e 10')
sleep(1)
print('Achas que sconsegue acertar???\n')
sleep(1)

while jogada!= CPU:
    tentativas+=1
    jogada=int(input('---> '))
    '''if jogada!=CPU:
        print('Errou!')'''
    if jogada > CPU:
        print('Mais abaixo!')
    elif jogada < CPU:
        print ('Mais abaixo>!')

print(f'Acertou! eu pensei em {CPU}, e conseguiu acertar!!!')
print(f'Total de tentativas: {tentativas}')








'''tentativas = 0
palpite = 1

print("Adivinhe o número entre 0 e 10!")

while palpite != numero_secreto:
    palpite = int(input("Digite seu palpite: "))
    tentativas = tentativas + 1

    if palpite != numero_secreto:
        print("Errado! Tente novamente.")

print("Parabéns! Você acertou!")
print("Tentativas:", tentativas)'''
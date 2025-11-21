'''Crie um programa que sorteie a ordem de
jogada num jogo ao “atirar um dado ao
ar”. Cada jogador terá um número
aleatório associado dentro de um
dicionário. No final ordene o ranking
para ver a ordem de jogada.'''


from random import randint
from time import sleep

# Cria o dicionário vazio
qtdJogadores =int(input('Digite quantos jogadores vão jogar: '))
jogadores = {}

# Sorteia valores
for c in range(qtdJogadores):
    nome= f'JOGADOR {c+1}' #input(f'Digite o nome do jogador {c+1}: ')
    jogada = randint(1,6)
    jogadores[nome] = jogada
#jogadores[input[f'Digite o nome do {c+1} jogador: ')] = randint (1,6)

auxiliar = jogadores.copy()
ranking = list()

while auxiliar:
    maior_jogador = ''
    maior_valor = 0

    for jogador, jogada in auxiliar.items():
        if jogada > maior_valor:
            maior_jogador = jogador
            maior_valor = jogada
    ranking.append((maior_jogador, maior_valor))
    del auxiliar[maior_jogador]

print(ranking)
[(j1,valor),(j2,valor)]

for tupla in ranking:
    for elemento in tupla:
        print(f'{elemento} ', end=' - ')
    sleep(1)
    print()








'''jogadores['Jogador 1'] = random.randint(1, 6)
jogadores['Jogador 2'] = random.randint(1, 6)
jogadores['Jogador 3'] = random.randint(1, 6)
jogadores['Jogador 4'] = random.randint(1, 6)

print("Valores sorteados:")
for j in jogadores:
    print(j, "tirou", jogadores[j])
    time.sleep(0.5)

# Transforma o dicionário em lista para ordenar
ranking = list(jogadores.items())

# Ordenação manual do maior para o menor (método simples)
for i in range(len(ranking)):
    for j in range(i + 1, len(ranking)):
        if ranking[j][1] > ranking[i][1]:
            aux = ranking[i]
            ranking[i] = ranking[j]
            ranking[j] = aux

print("\nRanking de jogada:")
posicao = 1
for item in ranking:
    print(posicao, "º lugar:", item[0], "com", item[1])
    posicao += 1'''
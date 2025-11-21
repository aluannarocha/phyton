'''Crie um programa que guarde o
aproveitamento de um jogador de
futebol. O programa deverá ler o nome,
quantos jogos jogou e a quantidade total de
golos e guardar tudo num
dicionário. No dicionário, deve
calcular a média de golos por jogo.'''

dados = {}

nome_jogador = input('Digite o nome do jogador: ')
qtd_jogos = int(input('Digite a quantidade de jogos que o jogador participou: '))
qtd_golos = int(input('Digite a quantidade total de golos: '))

dados["nome"] = nome_jogador
dados["jogos"] = qtd_jogos
dados["golos"] = qtd_golos


dados ["media"]= qtd_golos/qtd_jogos

print('O aproveitamento do jogador é', dados ["media"] )

'''for chave,valor in dados.items():
        print(f'{chave} = {valor}')'''






'''Melhore o exercício 67 para que permita
a entrada de vários jogadores. Defina um
sistema de visualização que permita ao
utilizador procurar pelos resultados de um
jogador específico.'''
jogadores = []

while True :
    dados = {}

    nome_jogador = input('Digite o nome do jogador: ')
    qtd_jogos = int(input('Digite a quantidade de jogos que o jogador participou: '))
    qtd_golos = int(input('Digite a quantidade total de golos: '))

    dados["nome"] = nome_jogador
    dados["jogos"] = qtd_jogos
    dados["golos"] = qtd_golos
    dados["media"] = qtd_golos / qtd_jogos

    jogadores.append(dados)

    print(f'O aproveitamento do jogador é {dados["media"]:.2f}')

    continuar = input("Deseja adicionar mais jogadores? (S/N): ").upper()
    if continuar == "N":
        break





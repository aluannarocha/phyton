'''Crie um programa que tenha um tuple com
nomes de jogos e os seus respetivos
preços em sequência.

No final, mostre uma listagem de preços
organizados como tabela.'''


jogos=(
    'Barbie', '40.40',
    'Digimon', '50.50',
    'Dragon Ball','60.60',
    'Crash','70.70',
    'Fifa', '80.80'
)

print(f'{"Lista de jogos":-^70}')
print('-'*70)
print(f'{" Jogo": <64}Preço')
print('-'*70)

for c in range (0,len(jogos)):
    if c % 2 == 0:
        print(f'{jogos[c]:.<64}', end='')
    else:
        print(f' {jogos[c]}')
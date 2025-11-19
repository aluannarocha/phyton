# estante = input('Digite uma consola: '), input('Digite outra consola: ')

nomes = ('Nádia', 'Laura', 'Alexandra', 'Telmo', 'Victor',
        'Rafael', 'Daniel', 'Leticia', 'Roman', 'Pedro',
        'Francisca', 'Inês')

'''for c in range(0, len(nomes)):
    print(f'No índice {c} está o nome: {nomes[c]}')

# OU

contador = 0

for nome in nomes:
    print(f'No índice {contador} está o nome: {nomes[contador]}')
    contador += 1'''



for c in range(0, len(nomes)):
    print(f'{c} -> {nomes[c]}')

for nome in nomes:
    print(nome)

for indice, nome in enumerate(nomes):
    print(f'No índice {indice} o valor é {nome}')

print(type(nomes))
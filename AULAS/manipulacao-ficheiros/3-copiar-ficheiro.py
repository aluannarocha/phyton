#ficheiro teste -> readline -> linhas

'''teste.txt -> abro em modo readline
linhas = teste.tt.readlines()

output aberto
for linha in linhas:
    output.write(linha)'''

from pathlib import Path

input_data = Path (r'ficheiro/teste.txt')
saida = Path(r'ficheiros/teste_copy.txt')

with input_data.open('r', encoding='utf-8', errors='ignore') as file:
    dados = file.readlines()

with saida.open('w',encoding='utf-8',errors='ignore') as out:
    for linha in dados:
        if 'amor' in linha.lower():
            out.write(linha)
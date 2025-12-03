# Importar o Pathlib
from pathlib import Path
# Criar a variável que representa o CAMINHO
caminho = Path(r'ficheiros/teste.txt')

with caminho.open('r', encoding='utf-8', errors ='ignore') as file:
    #print(file.readlines())
    for linha in file:
        print(linha, end='')

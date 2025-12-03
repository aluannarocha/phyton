import os

'''nome_pasta = 'ficheiros'

os.mkdir(nome_pasta)'''

#mkdir só cira uma pasta e é impossível criar ficheiro quando este já existe

caminho = 'ficheiros'
os.makedirs(caminho, exist_ok = True)

#makedirs pode criar multiplos ficheiros



from pathlib import Path # Classe Path que da métodos/funções típicas dde ficheiros

'''string = r'/Users/luannarocha/Desktop/phyton/AULAS/manipulacao-ficheiros/ficheiros'''
# Informar qual é o caminho do ficheiro
# Criar a variável que representa o caminho do ficheiro
caminho = Path(r'ficheiros/teste.txt')  #caminho relativo
print('Caminho criado com sucesso.')

'''caminho = Path (r'/Users/luannarocha/Desktop/phyton/AULAS/manipulacao-ficheiros/ficheiros') #caminho absoluto'''

# o Python cria o ficheiro se ele não existir
# Podemos abrir o ficheiro em modos diferentes:
#write - 'w' escrever
#read - 'r' escrever
#append - 'a' acrescentar

#no modo white apaga tudo que tiver e escreve

'''file = caminho.open()
file.write()
file.close()'''

with caminho.open('w', encoding ='utf-8', errors='ignore') as file:
    print('Ficheiro aberto em modo escrita com sucesso')
    file.write('Olá turma!!!\n')
    file.write('Olá novamente!!!\n')
    print('Mensagens escritas com sucesso')


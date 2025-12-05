'''Desenvolva um programa em python, de acordo com todas as boas práticas aprendidas,
que simule um bloco de notas.
O programa deve permitir:
1.Adicionar notas a um ficheiro .txt;
2.Mostrar todas as notas gravadas;
3.Apagar todas as notas;
4.Pesquisar notas por palavra-chave.
No final coloque o projeto no GitHub'''


import os
from pathlib import Path
from time import sleep

def cabecalho(txt: str):
    print('-' * 40)
    print(f'{txt:-^40}')
    print('-' * 40)

def cria_pasta() -> str: #originalmente queriamos criar várias pastas
    caminho = 'ficheiros'
    os.makedirs(caminho, exist_ok=True)

def verifica_existencia(nome_ficheiro: str) -> bool:
    '''

    Verifica se um ficheiro existe antes de efetuar qualquer ação

    '''

    caminho = Path(rf'ficheiros/{nome_ficheiro}.txt')
    existe = False
    if caminho.exists():
        existe = True
    else:
        print('Esse ficheiro não existe')

    return existe

def cria_ficheiro(nome_ficheiro: str):
    '''

    Cria um ficheiro .txt vazio

    '''
    caminho = Path(rf'ficheiros/{nome_ficheiro}.txt')
    with caminho.open('w', encoding='utf-8', errors='ignore') as file:
        file.write('')

def adicionar_nota(nome_ficheiro: str, conteudo: list):
    '''

    Adiciona conteudo a um certo ficheiro especificado pelo utilizador sem apagar o conteudo original

    '''

    temp = Path(rf'ficheiros/{nome_ficheiro}1.txt')
    original = Path(rf'ficheiros/{nome_ficheiro}.txt')

    with original.open('r', encoding='utf-8', errors='ignore') as file:
        dados = file.readlines()

    # faz uma copia do ficheiro
    with temp.open('w', encoding='utf-8', errors='ignore') as output:
        for linha in dados:
            output.write(linha)

    with original.open('w', encoding='utf-8', errors='ignore') as file:
        for linha in dados:
            file.write(linha)

        for linha in conteudo:
            file.write(f'{linha}\n')

    os.remove(temp) # remove o ficheiro temporario

def abrir_notas(nome_ficheiro: str):
    '''

    Faz print ao conteudo de um ficheiro .txt

    '''
    caminho = Path(rf'ficheiros/{nome_ficheiro}.txt')
    with caminho.open('r', encoding='utf-8', errors='ignore') as file:
        for linha_raw in file:
            linha_limpa = linha_raw.replace('\n', '') # elimina os \n em excesso
            print(linha_limpa)

def pesquisa_notas(nome_ficheiro: str, keyword: str):
    '''

    Pesquisa todo o conteudo dentro de um ficheiro .txt, caso a keyword exista numma linha
    print a linha toda

    '''
    caminho = Path(rf'ficheiros/{nome_ficheiro}.txt')
    with caminho.open('r', encoding='utf-8', errors='ignore') as file:
        for linha_raw in file:
            linha_limpa = linha_raw.replace('\n', '')  # elimina os \n em excesso
            if keyword in linha_limpa:
                print(linha_limpa)

def apagar_nota(nome_ficheiro: str):

    '''

    Copia da função cria_ficheiro mas com utilização diferente

    '''
    caminho = Path(rf'ficheiros/{nome_ficheiro}.txt')
    with caminho.open('w', encoding='utf-8', errors='ignore') as file:
        file.write('')

def apagar_ficheiro(nome_ficheiro: str):
    '''

    Apaga um ficheiro .txt especificado pelo utilizador

    '''
    caminho = Path(rf'ficheiros/{nome_ficheiro}.txt')
    os.remove(caminho)

cabecalho('Bloco de notas')
cria_pasta()
opcao = 0

while True:
    print('Escolha uma opção: ')
    print('[ 1 ] - Criar novo ficheiro')
    print('[ 2 ] - Adicionar Nota')
    print('[ 3 ] - Todas as notas')
    print('[ 4 ] - Pesquisar por palavra chave')
    print('[ 5 ] - Apagar notas')
    print('[ 6 ] - Apagar ficheiro')
    print('[ 7 ] - Sair')
    opcao = int(input('--> '))

    if opcao == 1: # novo ficheiro
        titulo_ficheiro = input('Digite um nome para o seu ficheiro: ')
        cria_ficheiro(titulo_ficheiro)

    elif opcao == 2: # adicionar nota
        lista = list()
        titulo_ficheiro = input('Qual o ficheiro que quer utilizar?\n--> ')
        print('Se a qualquer momento desejar guardar o seu ficheiro, digite [GUARDAR]')

        while True:
            content = input('--> ')
            if content == '[GUARDAR]':
                break
            else:
                lista.append(content)

        adicionar_nota(titulo_ficheiro, lista)

    elif opcao == 3: # todas as notas num ficheiro
        titulo_ficheiro = input('Qual o ficheiro que quer utilizar?\n--> ')
        existe = verifica_existencia(titulo_ficheiro)
        if existe:
            abrir_notas(titulo_ficheiro)

    elif opcao == 4: # pesquisa por palavra chave num ficheiro
        titulo_ficheiro = input('Qual o ficheiro que quer utilizar?\n--> ')
        existe = verifica_existencia(titulo_ficheiro)
        if existe:
            pesquisa = input('Pesquisa por uma palavra chave: ')
            pesquisa_notas(titulo_ficheiro, pesquisa)

    elif opcao == 5: # apaga todas as notas num ficheiro
        titulo_ficheiro = input('Qual o ficheiro que quer apagar?\n--> ')
        existe = verifica_existencia(titulo_ficheiro)
        if existe:
            apagar_nota(titulo_ficheiro)

    elif opcao == 6: # apagar um ficheiro
        titulo_ficheiro = input('Qual o ficheiro que quer apagar?\n--> ')
        existe = verifica_existencia(titulo_ficheiro)
        if existe:
            apagar_ficheiro(titulo_ficheiro)

    else: # encerra programa
        print('A encerrar', end='')
        sleep(0.5)
        print('.', end='')
        sleep(0.5)
        print('.', end='')
        sleep(0.5)
        print('.', end='')
        break
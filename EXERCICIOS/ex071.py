'''Crie um programa que tenha uma função
que receba um texto como parâmetro e que
mostre uma mensagem com tamanho
adaptável.

Ex:
mostre(“Olá mundo.”)
Saída:
-=-=-=-=-=-=-=-=
Olá mundo.
-=-=-=-=-=-=-=-='''

def cabecalho(texto):

    print('-='*20)
    print(f'{texto:-^40}')
    print('-='*20)

cabecalho(input('Digite um texto: '))

'''Crie um programa que leia 4 valores e
guarde-os num tuple. No final exiba:

a) Quantas vezes aparecer o número 7.
b) Em que posição foi digitado o número 5.
c) Quais são os números pares.

O programa deve informar quando não
encontrar resposta.'''
valores = (
    int(input('digite o primeiro valor: ')),
    int(input('digite o segundo valor: ')),
    int(input('digite o terceiro valor: ')),
    int(input('digite o quarto valor: ')))

qtd_setes=0
indice_cinco=''

TAM=len(valores)

for c in range (0,TAM):
    if valores[c]==7:
        qtd_setes+=1
    if valores [c] == 5:
        indice_cinco=c

if qtd_setes > 0:
    print(f'Foram digitados {atd_setes} setes')
else:
    print ('Não foram encontrados stetes')
if indice_cinco:
    print(f'O cinco foi digitado na {indice_cinco +1 } posição')
else:
    print('Não foi encontrado nenhum cinco')


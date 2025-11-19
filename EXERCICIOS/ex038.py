'''Faça um programa que leia uma frase
qualquer e diga se é um palíndromo,
desconsiderando os espaços.

Ex: Anotaram a data da maratona'''

frase=input('Digite uma frase: ').replace(' ','')
frase_reverse=''
tam =len(frase)
for c in range(tam,0,-1):
    frase_reverse+=frase[c-1]
print(frase_reverse)
if frase_reverse==frase:
    print('A frase é um palíndromo')
else:
    print('Não é um políndromo.')
'''Crie um programa que leia um número de
0 a 20 introduzido pelo utilizador.
Depois deverá mostrar por extenso o
número introduzido.'''


numeros= ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis',
         'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
         'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
numero= int(input('Digite um número de 0 a 20: '))
print (numeros[numero])

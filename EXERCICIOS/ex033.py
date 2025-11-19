'''Faça um programa que leia 5 números
inteiros e mostre a soma desses
números.'''


soma=0
for c in range(0,5):
    num=int(input(f'digite o {c+1} número: '))
    soma+= num    #é o mesmo que soma=soma+ num

print(soma)

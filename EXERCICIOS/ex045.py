'''Escreva um programa que leia um número
N inteiro qualquer e mostre os N
primeiros elementos de uma sequência
de Fibonacci.'''


numero = int(input("Digite quantos números da sequência de Fibonacci deseja ver: "))


num1 = 0
num2 = 1
contador = 0

print("Sequência de Fibonacci:")

while contador < numero:
    print(num1, end=" ")
    proximo = num1 + num2
    num1 = num2
    num2 = proximo
    contador = contador + 1

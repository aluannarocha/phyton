'''Crie um programa que leia vários
números inteiros e que termine apenas
quando o utilizador digitar a opção
para parar. No final mostre quantos
números o utilizador inseriu e qual a
soma entre eles.'''



quantidade = 0
soma = 0

while True:
    numero = int(input("Digite um número inteiro: "))

    soma = soma + numero
    quantidade = quantidade + 1

    resposta = input("Quer continuar? (s/n): ")

    if resposta == "n":
        break

print("Você digitou", quantidade, "números.")
print("A soma deles foi:", soma)




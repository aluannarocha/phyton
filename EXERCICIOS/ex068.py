'''Crie um programa que leia o nome, sexo e
idade de várias pessoas, guardando cada
dado num dicionário e todos os
dicionários numa lista. No final mostre:

a) Quantas pessoas foram registadas;
b) Qual a média de idades do grupo;
c) Quantas mulheres foram registadas;
d) Quantos homens com idade acima da média foram
registados.'''

pessoas = []   # lista para guardar vários dicionários

while True:
    dados = {}   # dicionário para uma pessoa

    dados["nome"] = input("Nome: ")
    dados["sexo"] = input("Sexo (M/F): ").upper()
    dados["idade"] = int(input("Idade: "))

    pessoas.append(dados)   # guardar o dicionário na lista

    continuar = input("Deseja continuar? (S/N): ").upper()
    if continuar == "N":
        break

# ----- Cálculos -----
total_pessoas = len(pessoas)

# média das idades
soma_idades = 0
for p in pessoas:
    soma_idades += p["idade"]

media_idades = soma_idades / total_pessoas

# contar mulheres
total_mulheres = 0
for p in pessoas:
    if p["sexo"] == "F":
        total_mulheres += 1

# homens com idade acima da média
homens_acima = 0
for p in pessoas:
    if p["sexo"] == "M" and p["idade"] > media_idades:
        homens_acima += 1

# ----- Resultados -----
print("\n--- RESULTADOS ---")
print("a) Pessoas registadas:", total_pessoas)
print("b) Média de idades:", media_idades)
print("c) Mulheres registadas:", total_mulheres)
print("d) Homens acima da média de idade:", homens_acima)



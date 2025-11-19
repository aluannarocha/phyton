'''Faça um programa que leia 10 números e
conte quantos deles são pares.'''

qtd_pares = 0

for c in range(0,10):
    numero = int(input(f"Digite o {c+1}º número: "))
    if numero % 2 == 0:
        qtd_pares += 1 #qtd_pares = qtd_pares + 1

# Exibe o resultado
print(f"Quantidade de números pares: {qtd_pares}")

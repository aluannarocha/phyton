'''Crie um programa que leia várias notas
introduzidas pelo utilizador. No final
mostre quantas notas o utilizador
inseriu, qual a média entre elas e
qual a maior e a menor nota.'''

print('~*º~*º Calculadora de Média de Notas º*~º*~')

nota=('')
contagem = soma = maior_nota = menor_nota = 0

while True:
    nota = float(input(f'Digite a {contagem+1}ª nota [0 para parar]: '))

    if nota == 0:
      break

    if contagem==0:
        maior_nota = menor_nota = nota

    else:
        if nota>maior_nota:
            maior_nota = nota

        if nota<menor_nota:
            menor_nota = nota

    contagem += 1
    soma += nota

media = soma / contagem

print(f'Inseriu {contagem} notas.')
print(f'Média: {media:.2f} valores.')
print(f'A maior nota inserida é: {maior_nota}')
print(f'A menor nota inserida é: {menor_nota}')

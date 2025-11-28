def soma_numeros (lista:list):
    soma = 0

    for numero in lista:
        soma += numero

    return soma

notas =[20,20,20,20,20]

media = soma_numeros (notas) / len(notas)

print(media)
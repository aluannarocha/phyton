#Contador que vai de 1 ate 10
contador=1
while contador<=10:
    print(contador)
    contador+=1


#Contador que vai de 10 até 0
contador=10
while contador>=0:
    print(contador)
    contador-=1


#Criar um programa que some todos os números digitador pelo utilizador
#Quantos? Não sie. Só sei que se o utilizador digitar 0, é para parar.
soma=0
numero=''
while numero!=0:
    numero=int(input('Digite um numero: '))
    soma+=numero
print(soma)


#eu quero criar um programa que peça o genero de uma pessoa
#apenas aceita como resposta F ou M
#se o utilizador digitar outra resposta ele vai ter de pedir novamente

genero=' '
while genero[0]!='M' and genero[0]!='F':
    genero=input('Digite seu genero: ').strip().upper()

'''#Quero criar um menu que o utilizador pode escolher 3 opções
#Escrever "olá", "tudo bem?", sair do programa.
opcao=''
while opcao !=3:
    print('---MENU---')
    print('[1]-Olá')
    print('[2]-Tudo bem?')
    print('[3]-Sair')
    opcao=int(input('---> '))
    
    if opcao==1:
        print('Olá')
    elif opcao==2:
        print('Tudo bem?')
    elif opcao==3:
        print('Saindo')
    else:
        print('Opção invalida!')'''


while True:
    print('---MENU---')
    print('[1]-Olá')
    print('[2]-Tudo bem?')
    print('[3]-Sair')
    opcao = int(input('---> '))

    if opcao == 1:
        print('Olá')
    elif opcao == 2:
        print('Tudo bem?')
    elif opcao == 3:
        print('Saindo')
        break
    else:
        print('Opção invalida!')


#Contagem de 0 até 1000
contador=0
while True:
    print(contador)
    contador+=1

    if contador==1000:
        print(1000)
        break



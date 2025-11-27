def cabecalho(texto):
    print('-'*20)
    print(f'{texto:-^20}')
    print('-'*20)


def soma(num1,num2):
    cabecalho('SOMA')
    print(f'{num1} + {num2} = {num1 + num2}')

def subtracao(num1,num2):
    cabecalho('SUBTRAÇÃO')
    print(f'{num1} - {num2} = {num1 - num2}')

def multiplicacao(num1,num2):
    cabecalho('MULTIPLICAÇÃO')
    print(f'{num1} * {num2} = {num1 * num2}')

def divisao(num1,num2):
    cabecalho('DIVISÃO')
    print(f'{num1} / {num2} = {num1 / num2}')


def menu():
    n1 = int(input('Digite um número: '))
    n2 = int(input('Digite outro número: '))

    while True:
        cabecalho('MENU')
        print('[1] - SOMA')
        print('[2] - SUBTRAÇÃO')
        print('[3] - MULTIPLICAÇÃO')
        print('[4] - DIVISÃO')
        print('[5] - SAIR')
        opcao = int(input('--> '))

        if opcao == 1:
            soma(num1=n1,num2=n2)
        elif opcao == 2:
            subtracao(num1=n1,num2=n2)
        elif opcao == 3:
            multiplicacao(num1=n1,num2=n2)
        elif opcao == 4:
            divisao(num1=n1,num2=n2)
        elif opcao == 5:
            print('A sair, volte sempre...')
            break

        else:
            print('Opção invalida')

menu()
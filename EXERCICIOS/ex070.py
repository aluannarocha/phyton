'''Crie um programa que tenha uma função chamada area()
que receba as dimensões de um terreno e mostre a area do terreno'''


def area():
    comprimento = float(input('Digite o comprimento do terreno: '))
    largura = float(input('Digite sua largura: '))
    area = comprimento * largura
    print(area)

area()
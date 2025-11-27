'''Crie um programa que tenha uma função chamada area()
que receba as dimensões de um terreno e mostre a area do terreno'''


'''def area():
    comprimento = float(input('Digite o comprimento do terreno: '))
    largura = float(input('Digite sua largura: '))
    area = comprimento * largura
    print(area)

area()'''


#parametro: typo de dado
def area (l: float, c:float):
    area_calculada=l*c
    print(f'A área deo terreno: {area_calculada:.2f}m2')

largura = float(input('Digite a largura do terreno: '))
comprimento = float(input('Digite o comprimento do terreno: '))

area(largura,comprimento)



'''Crie um programa que tenha uma função
que converta a temperatura de Celsius
para Fahrenheit.'''

def conversor(temp: float):
    fahrenheit = (temp * 1.8) + 32
    print(f'{temp}ºC equivalem a {fahrenheit}ºF')

temperatura_c = float(input('Digite a temperatura em celsius: '))

conversor(temperatura_c)
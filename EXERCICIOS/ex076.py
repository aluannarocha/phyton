'''Crie um programa que tenha uma função
que converta a temperatura de Celsius
para Fahrenheit.'''

def celsius_para_fahrenheit (celsius):
    fahrenheit = (celsius * 9/5) + 32
    print(f'{celsius}ºC equivalem a {fahrenheit}ºF')

temperatura_c = float(input('Digite a temperatura em celsius: '))

celsius_para_fahrenheit(temperatura_c)
'''Crie um programa com uma função que vai
funcionar como a função input(), no
entanto vai fazer a validação para
aceitar apenas um valor numérico.'''

def input_num(msg="Digite um número: "):
    while True:
        valor = input(msg)
        if valor.replace(".", "").isdigit():
            return float(valor)
        print("Erro! Digite apenas números.")


# Exemplo de uso
n = input_num ("Número: ")
print("Você digitou:", n)

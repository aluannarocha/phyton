'''Crie um programa com uma função chamada
fatorial(), que receba dois parâmetros:
o primeiro será o número a calcular o
fatorial e o segundo será opcional e
lógico que indique se será exibido ou
não o processo de cálculo do fatorial. O
fatorial deve ser guardado num ficheiro
txt.'''

def fatorial(n, mostrar=False):
    """
    Calcula o fatorial de n.
    Se mostrar=True, exibe o processo passo a passo.
    Guarda o resultado num ficheiro fatorial.txt.
    """
    f = 1
    processo = ""

    for c in range(n, 0, -1):
        f *= c
        if mostrar:
            processo += f"{c} x " if c > 1 else f"{c} = "

    # Criar mensagem final
    if mostrar:
        processo += str(f)
        resultado_texto = f"Fatorial de {n}:\n{processo}"
    else:
        resultado_texto = f"Fatorial de {n} = {f}"

    # Guardar no ficheiro
    with open("fatorial.txt", "w", encoding="utf-8") as ficheiro:
        ficheiro.write(resultado_texto)

    return f


# Exemplo de uso:
numero = int(input("Digite um número para calcular o fatorial: "))
mostrar_proc = input("Deseja mostrar o processo? (s/n): ").lower() == 's'

resultado = fatorial(numero, mostrar_proc)
print(f"Resultado guardado em 'fatorial.txt'. Valor calculado: {resultado}")

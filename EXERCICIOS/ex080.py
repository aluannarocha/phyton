'''Crie um programa com uma função que vai
receber várias notas de alunos e vai
retorna um dicionário com o seguinte:

a) Quantidade de notas
b) A maior nota
c) A média da turma
d) A situação (lógico opcional)
>12 – boa
<9,5 – fraca
>9,5 e <12 - razoável'''

def analisar_notas(*notas, situacao=False):
    resultado = {}

    resultado['quantidade'] = len(notas)
    resultado['maior_nota'] = max(notas)
    media = sum(notas) / len(notas)
    resultado['media'] = media

    if situacao:
        if media > 12:
            resultado['situacao'] = 'boa'
        elif media < 9.5:
            resultado['situacao'] = 'fraca'
        else:
            resultado['situacao'] = 'razoável'

    return resultado


# Exemplo de uso
dados = analisar_notas(10, 14, 12, 9, 11, situacao=True)
print(dados)
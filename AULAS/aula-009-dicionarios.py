turma=[]
qtd_alunos = 5
aluno = dict()  # ou {}

for c in range (qtd_alunos):


    aluno['nome'] = input(f'Digite o nome do aluno {c+1}: ')
    aluno['media'] = float(input(f'Digite a media do {aluno["nome"]}: '))

    #situação com OPERADOR TERNÁRIO
    aluno['situaçãp']= 'Aprovado' if aluno['media'] >=9.5 else 'Reprovado'

    #Situação com IF NORMAL
    '''if aluno['media'] >= 9.5:
        aluno['situação'] = 'Aprovado'
    else:
        aluno['Situação'] = 'Reprovado' '''

    turma.append(aluno.copy())

print(turma)


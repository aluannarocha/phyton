
from math import fsum

notas=list()
print(type(notas))


for c in range (0,5):
    nota=float(input(f'Digite a {c+1} nota: '))
    notas.append(nota)
media=fsum(notas)/len(notas)
print (media)


-------------

serues=list()
print('Inere o teu top 5 de séries: ')
for c in range(0,5):
    serie=input(f'{c+1}--> ')
    series.append(serie)
print(series)

while True:
    print('1-Inserir novo top 5')
    print('2-Substituir serie')
    print('3-Mostrar top 5')
    print('4-Sair')
    opcao=int(input('---> '))

    match opcao:
        case 1:
            print('Inere o teu top 5 de séries: ')
            for c in range(0, 5):
                serie = input(f'{c + 1}--> ')
                series.append(serie) 2:
        case 2:
    
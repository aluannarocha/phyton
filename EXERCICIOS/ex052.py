'''Crie um programa com um tuple com os 20
primeiros classificados do Campeonato
Espanhol de Futebol. Depois mostre:

a) Os primeiros 5 classificados.
b) Os últimos 4 classificados.
c) Uma lista com as equipas por ordem alfabética.
d) A posição da equipa Las Palmas.'''

times=('REAL MADRID','BARCELONA','VILLARREAL','BETIS','ATHETIC BILBAO','ELCHE','ATLETICO DE MADRID',
       'SEVILLA','ESPANHOL','ALAVES','GETAFE','OSASUNA','LEVANTE','RAYO VALLECANO',
       'VALENCIA','CELTA','GIRONA','REAL OVIEDO','REAL SOCIEDAD','MALLORCA')

print('---5 primeiros classificados---')
for indice, equipa in enumerate(times):
    if indice==5:
        break
    else:
        print(f'\t{indice+1} - {equipa}')
print('-------------------------------------')

#os 4 ultimos classificados == len(equipas)-1
#o penultimo classificado ==len(equipas) - 2
#o anti penultimo classificado == len(equipas) -3

print('---5 primeiros classificados---')
TAM = len(times)
for indice, equipa in enumerate(times):
    if indice >= TAM - 4:
        print(f'\t{indice + 1} - {equipa}')
    else:
        continue
print('-----------------------------------')
print('TIMES POR ORDEM ALFABÉTICA')
for equipa in sorted(times):
    print('\t',equipa)

print ('----------------------------------')

print('Posição equipa Las Palmas: ')
esta_la = False
indice_las_palmas =''
for indice, equipa in enumerate(times):
    if equipa == 'LAS PALMAS':
        esta_la = True
        indice_las_palmas=indice
if esta_la == True :
    print(f'Las Palmas -> {indice_las_palmas+1}lugar')
else:
    print('Las palmas não está clasificada')





'''while True:
    print('---5 primeiros classificados---')
    if times:
        for c in range (0,5):
            print(f'{c+1} - {times[c]}')
        break
while True:
    print('---5 primeiros classificados---')
    if times:
        for c in range (16,20):
            print(f'{c+1} - {times[c]}')
        break



for c in range(0, 5):
    print(f'Os primeiros 5 classificados são: {times[c]}')
for c in range(16,20):
    print(f'Os últimos 4 classificados são: {times[c]}')'''
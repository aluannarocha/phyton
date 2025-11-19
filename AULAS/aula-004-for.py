#range(inicio, fim, passo)
from time import sleep

for c in range(0,5):
    print(c+1) #nao mostrar o zero
    sleep(1)

for c in range (5,0,-1):
    print(c)

soma=0
for c in range(0,5):
    nota=float(input(f'digite a {c+1} nota: '))
    soma+= nota    #é o mesmo que soma=soma+ nota

print(soma)

for c in range(0,10):
    print(f'{numero}x{c+1}={numero*(c+1)}')
    input()
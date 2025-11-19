'''Desenvolva um programa que faça 3
perguntas ao utilizador e apenas
aceite como resposta “V” ou “F”. Caso
esteja errado, peça para repetir a
resposta até ter um valor correto.'''


resposta=''
print('O céu é azul?')

while resposta!='V' and resposta!='F':
    resposta=input('[V/F]: ').strip().upper()
    if resposta=='V':
        print('Acertou!Vamos a próxima.')
    elif resposta=='F':
        print('Eroou!')
    else:
        print('Resposta inválida.')

resposta=''
print('O mar é laranja??')

while resposta!='V' and resposta!='F':
    resposta=input('[V/F]: ').strip().upper()
    if resposta=='V':
        print('Errou.')
    elif resposta=='F':
        print('Acertou!Vamos a próxima.')
    else:
        print('Resposta inválida.')


print('O formador é o Ricardo?')
while True:
    resposta=input('[V/F]: ').strip().upper()
    if resposta=='V':
        print('Acertou!Fim.')
        break
    elif resposta=='F':
        print('Eroou!')
    else:
        print('Resposta inválida.')



import time
print('---Boas vindas!!!---')
time.sleep(1)
print('Faça o seu registo!')
username_in=input('username: ').strip()
email_in=input('email: ').strip()
if email_in.count('@')==0 and email_in.count('.') ==0:
    print('email inválido, insira novamente.')
    email_in=input('email: ').strip()
password_in=input('password: ').strip()
if username_in == password_in:
    print('A password está igual ao username')
    password_in:input('password: ').strip()

time.sleep(0.5)
print('Criando seu perfil', end='')
time.sleep(0.5)
print('.', end='')
time.sleep(0.5)
print('.', end='')
time.sleep(0.5)
print('.', end='')
time.sleep(0.5)
print('Registo efetuado com sucesso, vamos reencaminhar para o loguin.')

print('---MENU---')
print('[1]-loguin')
print('[2]-sair')
opcao=input('--> ').strip().lower()

if opcao== 'loguin' or opcao=='1':
    username=input('username: ').strip()
    email=input('email: ').strip()
    password=input('password: ').strip()
    if username==username_in and email==email_in and password==password_in:
        print('Loguin efetuado com sucesso!')
    else:
        print('Tem algo errado, tente novamente!')
        username=input('username: ').strip()
        email=input('email: ').strip()
        password=input('password: ').capitalize().strip()
        if username==username_in and email==email_in and password==password_in:
            print('Loguin efetuado com sucesso>>!')
        else:
            print('Conta bloqueada! Fim do programa.')

elif opcao=='sair' or opcao=='2':
    print('Obrigado por utilizar o nosso programa! Tenha um bom dia!!!')
else:
    print('Opção inválida.')

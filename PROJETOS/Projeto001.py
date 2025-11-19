print('---Índice de Massa Corporal(IMC).---')
altura=float(input('Qual sua altura em metros?'))
peso=float(input('Qual seu peso em kg?'))
imc=peso/(altura*altura)
if imc < 18.5:
    print(f'"Abaixo do peso" Seu imc é {imc:.2f}!')
elif imc < 24.9:
        print(f'"Peso normal" Seu imc é {imc:.2f}!')
elif imc < 29.9:
        print(f'"Sobrepeso" Seu imc é {imc:.2f}!')
elif imc < 34.9:
        print(f'"Obesidade grau 1" Seu imc é {imc:.2f}!')
elif imc <= 39.9:
        print('"Obesidade grau 2"')
else:
        print('"Obesidade grau 3 (obesidade mórbida)"')
from math import pow
peso = float(input('Digite o seu peso'))
altura = float(input('Digite a sua altura'))
imc = peso/pow(peso, 2)
if imc < 18.5:
    print('Você está abaixo do peso')
elif 18.5 <= imc <= 25:
    print('Você está no peso ideal')
elif 25 < imc <= 30:
    print('Você está no sobrepeso')
elif 30 < imc <= 40:
    print('Você está em estado de obesidade!')
else:
    print('Você está em estado de obesidade mórbida')
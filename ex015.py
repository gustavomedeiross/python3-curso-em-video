kmp = float(input('Quantos kilômetros você percorreu?'))
dias = float(input('Quantos dias você ficou com o carro?'))
print('Você deve pagar R${:.2f}.'.format(dias*60+kmp*0.15))
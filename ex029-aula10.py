print('O limite de velocidade dessa via é de 80km/h')
v = int(input('Qual é a velocidade que você está andando?'))
if v >= 80:
    print('Você foi multado!\nVocê deve pagar R${}'.format((v-80)*7))
else:
    print('Muito bem! Você está dirigindo no limite correto!')
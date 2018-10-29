d = int(input('Qual é a distância da viagem (em km)?'))
if d <= 200:
    print('O preço da passagem será R${}.'.format(d*0.5))
else:
    print('O preço da viagem será de R${}.'.format(d*0.45))

idade = int(input('Quantos anos você tem?'))
if idade < 18:
    print('Falta {} anos pra você se alistar!'.format(18-idade))
elif idade == 18:
    print('Vá se alistar nesse ano!')
elif idade > 28:
    print('Você não precisa mais se alistar!')
    
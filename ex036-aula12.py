valordacasa = float(input('Qual é o valor da casa que você deseja comprar?'))
salario = float(input('Qual é o seu salário mensal?'))
qntparcelas = int(input('Em quantos anos você pretende pagar?'))
qntparcelas = qntparcelas*12
prestacaomensal = valordacasa/qntparcelas
taxadeaprovacao = salario*0.3
if prestacaomensal <= taxadeaprovacao:
    print('Muito bem! O valor da parcela mensal será de {:.2f}'.format(prestacaomensal))
else:
    print('Infelizmente, não será possível realizar o empréstimo.')
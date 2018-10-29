pdp = float(input('Qual é o preço padrão do produto?'))
mdp = input('Qual é o método de pagamento?')
x = input('Em quantas vezes será feito?')
y = x.isnumeric()
if y == True:
    x = int(x)

if mdp == 'cheque' or mdp == 'dinheiro':
    if x =='à vista':
        print('O preço do produto será R${:.2f}'.format(pdp-pdp*0.1))
    else:
        print('Esse método de pagamento não está disponível')
elif mdp == 'cartão':
    if x == 'à vista':
        print('O preço à ser pago é R${}'.format(pdp - pdp * 0.05))
    elif x == 2:
        print('O preço à ser pago é R${}'.format(pdp))
    elif x >= 3:
        print('O preço à ser pago é R${}'.format(pdp + pdp * 0.2))


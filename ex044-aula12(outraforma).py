preço = float(input('Preço do produto: R$'))
condiçãodepagamento = int(input('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão
Qual é a opção? '''))
if condiçãodepagamento == 1:
    print(f'Sua compra de R${preço:.2f} vai custar R${preço - preço*0.1:.2f} no final')
elif condiçãodepagamento == 2:
    print(f'Sua compra de R${preço:.2f} vai custar R${preço*0.05:.2f}')
elif condiçãodepagamento == 3:
    print(f'Sua compra irá custar R${preço:.2f}')
elif condiçãodepagamento == 4:
    parcelasdocartão = int(input('Quantas parcelas? '))
    preçodocartão = preço + preço * 0.2
    preçodaparcela = preçodocartão / parcelasdocartão
    print(f'''Sua compra será parcelada em 10x de R${preçodaparcela:.2f} com juros
Sua compra de R${preço:.2f} vai custar R${preçodocartão:.2f} no final''')
else: print('\033[31mForma de pagamento inválida\033[m')

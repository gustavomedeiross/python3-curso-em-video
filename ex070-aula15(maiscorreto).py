total = tot1000 = maisbarato = cont = 0
nomemaisbarato = ''
while True:
    produto = str(input('Nome do Produto: ')).title()
    preço = float(input('Preço: R$'))
    total += preço
    if preço > 1000:
        tot1000 += 1
    if preço == maisbarato:
        nomemaisbarato += f' {produto}'
    if cont == 0 or preço < maisbarato:
        maisbarato = preço
        nomemaisbarato = produto
    cont += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print(f'{"FIM DO PROGRAMA":=^40}')
print(f'O total da compra foi R${total:.2f}')
print(f'Ao todo, tiveram {tot1000} produtos acima de R$1000,00')
print(f'O produto mais barato foi {nomemaisbarato} que custou R${maisbarato:.2f}')

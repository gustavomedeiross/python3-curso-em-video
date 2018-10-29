alt = float(input('Qual é a altura da parede?'))
lar = float(input('Qual é a largura da parede?'))
area = alt*lar
#balde = 18L
#1 litro pinta 2 m²... quantos litros precisa para pintar a parede?
#preço do balde = R$250,00
print('Você irá pintar uma parede de {} metros quadrados.'.format(area))
qbalder = (area/2)/18 #quantidade utilizada de baldes
qbaldei = ((area/2)//18)+1 #quantidade de baldes inteiros
print('Para isso, você precisará comprar {:.2f} baldes de 18L, afinal será necessário {:.2f} litros de tinta.'.format(qbaldei, area/2))
print('O gasto de tinta utilizada (considerando balde = R$250,00) será de R${:.2f}, mas o gasto real será de R${:.2f}.'.format(qbalder*250, qbaldei*250))

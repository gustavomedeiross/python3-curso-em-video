preço = preçototal = contprodutos1000 = menor = cont =  0
while True:
   cont += 1
   nome = input('Digite o nome do produto: ').strip().capitalize()
   preço = float(input('Digite o preço do produto: R$'))
   if preço > 1000:
       contprodutos1000 += 1
   if cont <= 1:
       menor = preço
   else:
       if preço < menor:
           menor = nome

   preçototal += preço

   qrcntn = input('Você comprou mais produtos? [S/N]').strip().upper()[0]
   while qrcntn not in 'SN':
       qrcntn = input('Resposta inválida. Você comprou mais produtos? [S/N]').strip().upper()[0]
   if qrcntn == 'N':
       break

print(f'''Total gasto na compra: R${preçototal:.2f}
Quantidade de Produtos acima de R$1000,00: {contprodutos1000}
Produto mais barato: R${menor:.2f}''')
print('=====FIM=====')

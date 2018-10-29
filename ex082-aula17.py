lista = list()
while True:
   lista.append(int(input('Digite um valor: ')))
   qrcnt = input('Você quer continuar? [S/N]').upper().strip()[0]
   while qrcnt not in 'SN':
       qrcnt = input('\033[31mValor inválido.\033[m Você quer continuar? [S/N]').upper().strip()[0]
   if qrcnt == 'N':
       break
listapar = list()
listaímpar = list()
for pos in range(0, len(lista)):
   if lista[pos] % 2 == 0:
       listapar.append(lista[pos])
   else:
       listaímpar.append(lista[pos])

print(f'A lista completa é {lista}')
print(f'A lista de pares é {listapar}')
print(f'A lista de ímpares é {listaímpar}')
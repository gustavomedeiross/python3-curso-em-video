lista = list()
while True:
   lista.append(int(input('Digite um número: ')))
   qrcnt = input('Você quer continuar? [S/N]').upper().strip()[0]
   while qrcnt not in 'SN':
       qrcnt = input('Você quer continuar? [S/N]').upper().strip()[0]
   if qrcnt == 'N':
       break

print(f'A quantidade de números digitados foram {len(lista)}')
lista.sort(reverse=True)
print(f'A lista completa, ordenada de trás pra frente é {lista}')
if 5 in lista:
   print('O valor 5 está na lista!')
else:
   print('O valor 5 não foi encontrado na lista!')
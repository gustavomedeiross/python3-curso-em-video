pessoas = []
dado = []
leve = pesado = 0

while True:
   dado.append(str(input('Nome: ')).capitalize())
   dado.append(float(input('Peso: ')))
   if len(pessoas) == 0:
       pesado = leve = dado[1]
   else:
       if dado[1] > pesado:
           pesado = dado[1]
       elif dado[1] < leve:
           leve = dado[1]

   pessoas.append(dado[:])
   dado.clear()
   qrcnt = str(input('Quer continuar? [S/N]')).strip().upper()[0]
   while qrcnt not in 'SN':
       qrcnt = str(input('\033[31mResposta Inválida.\033[mQuer continuar? [S/N]')).strip().upper()[0]
   if qrcnt == 'N':
       break
print('-=' * 30)
print(f'A quantidade de pessoas cadastradas foram {len(pessoas)}')

print(f'O maior peso foi o de {pesado}kg. Peso de', end=' ')
for p in pessoas:
   if p[1] == pesado:
       print(p[0], end=' ')
print()
print(f'O menor peso foi o de {leve}kg. Peso de', end=' ')
for p in pessoas:
   if p[1] == leve:
       print(p[0], end=' ')
print()

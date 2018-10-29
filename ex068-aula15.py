from random import randint
print('''=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
   VAMOS JOGAR PAR OU ÍMPAR?
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=''')
cont = 0
while True:
   valor = int(input('Diga um valor! ='))
   humano = input('Par ou Ímpar? [P/I]').strip().upper()[0]
   pc = randint(0, 10)
   resultado = (valor+pc) % 2

   if humano == 'P':
       if resultado == 0:
           break
       if resultado != 0:
           print('O computador ganhou!')
   elif humano == 'I':
       if resultado != 0:
           break
       if resultado == 0:
           print('O computador ganhou!')
   else:
       print('Você digitou um valor inválido. Digite outro valor novamente!')
   cont += 1
   print(f'O computador jogou {pc}')

print(f'VOCÊ VENCEU! O computador ganhou {cont} vezes consecutivas!')


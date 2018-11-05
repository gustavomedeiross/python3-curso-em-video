from random import randint
print('''=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
   VAMOS JOGAR PAR OU ÍMPAR?
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=''')
cont = 0
while True:
   valor = int(input('Diga um valor! ='))
   humano = input('Par ou Ímpar? [P/I]').strip().upper()[0]
   while humano not in 'PI':
       humano = input('Par ou Ímpar? [P/I]').strip().upper()[0]
   pc = randint(0, 10)
   resultado = (valor+pc) % 2
   if humano == 'P':
       if resultado == 0:
           cont += 1
           print('Você venceu!')
       if resultado != 0:
           print('O computador venceu!')
           break
   elif humano == 'I':
       if resultado != 0:
           cont += 1
           print('Você venceu!')
       if resultado == 0:
           print('O computador ganhou!')
           break
   print(f'O computador jogou {pc}')
print(f'GAME OVER! Você ganhou {cont} vezes!')

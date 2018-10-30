#o exercício não funciona totalmente porque o "choices" pode repetir... portanto, o correto seria ter utilizado o "sample"
#sample não repete//choices repete.
#broken
from random import choices
from time import sleep
opções = list(range(0, 61))
dado = []
print('-' * 30)
print(f'{"JOGO DA MEGA SENA":^30}')
print('-' * 30)
n = int(input('Quantos jogos você quer que eu sorteie?'))
print('-=' * 6, f' SORTEANDO {n} JOGOS ', '=-' * 6)
for c in range(0, n):
   dado.append(choices(opções, k=6))
   dado[0].sort()
   sleep(1.5)
   print(f'Jogo {c+1}: {dado[0]}')
   dado.clear()
print('-=' * 10, '< BOA SORTE! >', '=-' * 10)

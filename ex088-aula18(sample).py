from random import sample
from time import sleep
jogos = list()
print('-' * 30)
print(f'{"JOGO DA MEGA SENA":^30}')
print('-' * 30)
n = int(input('Quantos jogos você quer que eu sorteie?'))
print('-=' * 6, f' |SORTEANDO {n} JOGOS| ', '=-' * 6)
for c in range(0, n):
   a = sorted(sample(range(1, 61), 6))
   jogos.append(a[:])
   print(f'Jogo {c+1}: {a}')
   sleep(0.5)
print('-=' * 10, '< BOA SORTE! >', '=-' * 10)

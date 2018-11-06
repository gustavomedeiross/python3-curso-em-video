from time import sleep
from random import choice
from operator import itemgetter
dado = range(1, 7)
jogadores = {'jogador1': choice(dado),
             'jogador2': choice(dado),
             'jogador3': choice(dado),
             'jogador4': choice(dado)}
ranking = list()
print('Valores Sorteados:')
sleep(1)
for k, v in jogadores.items():
    print(f'O {k} tirou {v}')
    sleep(1)
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print('-=' * 30)
print('  === RANKING DOS JOGADORES ===')
for i, v in enumerate(ranking):
    print(f'  {i+1}º lugar: {v[0]} com {v[1]}.')
    sleep(1)

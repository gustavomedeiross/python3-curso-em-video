from random import randint
from time import sleep
números = []


def sorteia():
    print('Sorteando 5 valores da lista: ', end='')
    for c in range(0, 5):
        números.append(randint(0, 10))
        print(números[c], end=' ')
        sleep(0.5)
    print()
def somaPar():
    somadospares = 0
    for c in range(0, len(números)):
        if números[c] % 2 == 0:
            somadospares += números[c]
    print(f'Somando os valores pares de {números}, temos {somadospares}')


sorteia()
somaPar()

from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
jogador = int(input('''Digite a sua escolha!
[ 1 ] Pedra
[ 2 ] Papel
[ 3 ] Tesoura ''')) - 1
print(f'Você escolheu {itens[jogador]}!')
print('Jo')
sleep(1)
print('Ken')
sleep(1)
print('Pô!')
sleep(1)
if computador + 1 == jogador or computador - 2 == jogador:
    print('Você venceu!')
elif jogador + 1 == computador or jogador - 2 == computador:
    print('O computador venceu!')
elif computador == jogador:
    print('EMPATE!')
print(f'O computador escolheu {itens[computador]}')

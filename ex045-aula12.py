from random import choice
from time import sleep
computador = choice(['Papel', 'Tesoura', 'Pedra'])
escolha = str(input('Escolha: Pedra, Papel ou Tesoura!'))
esc = escolha.title()
print('Pedra papel tesooou...')
sleep(1)
print('...uuura!!')
sleep(1)
if esc == 'Tesoura' and computador == 'Papel':
    print('\033[32mVocê venceu!\033[m')
elif esc == 'Papel' and computador == 'Pedra':
    print('\033[32mVocê venceu!\033[m')
elif esc == 'Pedra' and computador == 'Tesoura':
    print('\033[32mVocê venceu!\033[m')

elif esc == computador:
    print('\033[33mVocês empataram!\033[m')

else:
    print('\033[31mVocê perdeu!\033[m')

print('O computador escolheu {}'.format(computador))


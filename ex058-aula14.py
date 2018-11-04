from random import randint
print('Tente adivinhar o número que o computador pensou! [0-10]')
nc = randint(0, 10)
tentativa = -1
s = 0
while tentativa != nc:
    tentativa = int(input('Digite o número que o computador pensou: '))
    s += 1
    if tentativa != nc:
        print('\033[1;31mVocê errou! Tente novamente!\033[m')
print('\033[1;32mVocê acertou! Foram necessárias {} tentativas para acertar'.format(s))

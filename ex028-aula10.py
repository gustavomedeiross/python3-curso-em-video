import random
n = random.randint(0, 10)
nu = int(input('Qual número o computador escolheu?'))
if n == nu:
    print('Você venceu!')
else:
    print('O computador venceu!')
    print('O número era {}'.format(n))




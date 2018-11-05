números = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
           'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    n = int(input('Digite um número entre 0 e 20: '))
    while n < 0 or n > 20:
        n = int(input('Erro. Digite novamente'))
    print(f'Você digitou o número {números[n]}')
    qrcnt = ' '
    while qrcnt not in 'SsNn':
        qrcnt = str(input('Você quer continuar? [S/N]')).strip()[0]
    if qrcnt in 'Nn':
        break
print(f'{"FIM":=^30}')

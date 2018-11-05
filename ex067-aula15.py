núm = 0
while True:
    núm = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 30)
    if núm < 0:
        break
    for x in range(1, 11):
        print(f'{núm} x {x} = {núm * x}')
    print('-' * 30)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')

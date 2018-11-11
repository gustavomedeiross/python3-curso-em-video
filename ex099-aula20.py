from time import sleep


def maior(*núm):
    print('-=' * 30)
    print('Analisando os valores passados...')
    for c in núm:
        print(c, end=' ')
        sleep(0.2)
    print()
    print(f'Foram informados {len(núm)} valores ao todo.')
    if len(núm) == 0:
        print(f'O maior valor informado foi 0')
    else:
        print(f'O maior valor informado foi {max(núm)}')
    sleep(0.5)


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()

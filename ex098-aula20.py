from time import sleep


def contador(início, fim, passo):
    print('-=' * 20)
    if passo == 0:
        passo = 1
    print(f'Contagem de {início} até {fim} de {passo} em {passo}')
    if fim < início and passo > 0:
        passo = passo * -1
    if início > fim:
        fim = fim - 1
    else:
        fim = fim + 1
    for c in range(início, fim, passo):
        print(c, end=' ')
        sleep(0.5)
    print('FIM!')


#Programa principal
contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é sua vez de personalizar a contagem!')
contador(int(input('Início: ')), int(input('Fim: ')), int(input('Passo: ')))

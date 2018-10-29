lista = list()
while True:
    núm = int(input('Digite um valor: '))
    if núm in lista:
        print('Valores duplicados não serão adicionados!')
    if núm not in lista:
        lista.append(núm)
        print('Valor registrado com sucesso!')
    qrcnt = input('Você quer continuar? [S/N]').upper().strip()[0]
    while qrcnt not in 'SN':
        qrcnt = input('Resposta inválida. Você quer continuar?').upper().strip()[0]
    if qrcnt == 'N':
        break

print('=-' * 40)
lista.sort()
print(f'Os valores registrados foram {lista}')

pessoas = []
dado = []
maispesados = []
maisleves = []
pesado = leve = cont = 0

while True:
    dado.append(str(input('Nome: ')).capitalize())
    dado.append(float(input('Peso: ')))
    pessoas.append(dado[:])
    #peso
    if cont == 0:
        leve = pesado = dado[1]
        maispesados.append(dado[:])
        maisleves.append(dado[:])
    else:
        if dado[1] == pesado:
            maispesados.append(dado[:])
        elif dado[1] == leve:
            maisleves.append(dado[:])
        elif dado[1] > pesado:
            maispesados.clear()
            maispesados.append(dado[:])
            pesado = dado[1]
        elif dado[1] < leve:
            maisleves.clear()
            maisleves.append(dado[:])
            leve = dado[1]

    dado.clear()
    cont += 1
    qrcnt = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    while qrcnt not in 'SN':
        qrcnt = str(input('\033[31mResposta Inválida.\033mQuer continuar? [S/N]')).upper().strip()[0]
    if qrcnt == 'N':
        break

print('-=' * 30)
print(f'Ao todo, foram cadastradas {len(pessoas)} pessoas')
print(f'O maior peso foi de {pesado}kg. Peso de', end=' ')
for c in range(0, len(maispesados)):
    print(maispesados[c][0], end=' ')
print()
print(f'O menor peso foi de {leve}kg. Peso de', end=' ')
for c in range(0, len(maisleves)):
    print(maisleves[c][0], end=' ')
print()

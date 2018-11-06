jogadores = list()
jogador = dict()
gols = list()
total = 0
while True:
    jogador['nome'] = str(input('Nome do Jogador: ')).capitalize()
    númdepartidas = int(input(f'Quantas partidas {jogador["nome"]} jogou?'))
    for c in range(0, númdepartidas):
        gols.append(int(input(f'Quantos gols na partida {c+1}?')))
        total += gols[c]
    jogador['gols'] = gols[:]
    gols.clear()
    jogador['total'] = total
    total = 0
    jogadores.append(jogador.copy())
    qrcnt = ' '
    while qrcnt not in 'SsNn':
        qrcnt = input('Quer continuar? [S/N]')
    if qrcnt in 'Nn':
        break
print(jogadores)

jogadores = list()
jogador = dict()
gols = list()
total = 0
while True:
    print('-' * 30)
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
print('-=' * 30)
print(f'{"Código":<9}{"Nome":<10}{"Gols":<20}{"Total":<7}')
print('-' * 40)
for c in range(0, len(jogadores)):
    print(f'{c:<8} {jogadores[c]["nome"]:<10}{str(jogadores[c]["gols"]):<20}{jogadores[c]["total"]:<7}')
print('-' * 40)
while True:
    dados = int(input('Mostrar dados de qual jogador? (999 fecha o programa): '))
    if dados in range(0, len(jogadores)):
        print(f'==LEVANTAMENTO DO JOGADOR {jogadores[dados]["nome"]}:')
        for c in range(0, len(jogadores[dados]['gols'])):
            print(f'    No jogo {c+1} fez {jogadores[dados]["gols"][c]} gols')
    elif dados == 999:
        break
    else:
        print('\033[31mJogador Inválido. Tente novamente.\033[m')
print('Obrigado por utilizar programa de análise de jogadores! Volte sempre!')

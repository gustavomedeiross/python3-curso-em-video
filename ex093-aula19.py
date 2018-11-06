jogador = dict()
gols = list()
total = 0
jogador['nome'] = str(input('Nome do Jogador: ')).capitalize()
númdepartidas = int(input(f'Quantas partidas {jogador["nome"]} jogou?'))
for c in range(0, númdepartidas):
    gols.append(int(input(f'Quantos gols na partida {c+1}?')))
    total += gols[c]
jogador['gols'] = gols
jogador['total'] = total
print('-=' * 30)
print(jogador)
print('-=' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')
print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {númdepartidas} partidas')
for pos, x in enumerate(gols):
    print(f'    => Na partida {pos+1}, fez {x} gols')
print(f'Foi um total de {jogador["total"]} gols')

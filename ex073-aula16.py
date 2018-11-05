times = ('Palmeiras', 'Flamengo', 'Internacional', 'São Paulo', 'Grêmio', 'Atlético Mineiro', 'Santos', 'Atlético-PR',
         'Fluminense', 'Cruzeiro', 'Bahia', 'Corinthians', 'Botafogo', 'Vasco da Gama', 'América-MG', 'Vitória',
         'Ceará', 'Chapecoense', 'Sport Recife', 'Paraná')
marquinha = '-=' * 20
print(marquinha)
print(f'Os 5 primeiros colocados no brasileirão são: {times[0:5]}')
print(marquinha)
print(f'Os 4 últimos da tabela são: {times[-4:]}')
print(marquinha)
print(sorted(times))
print(marquinha)
print(f'A Chapecoense está em {times.index("Chapecoense")+1}º lugar')
print(marquinha)

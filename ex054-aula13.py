from datetime import date
smai = 0
smen = 0
hj = date.today().year
for c in range(0, 7):
    ano = int(input('Digite que ano você nasceu: '))
    if hj - ano >= 21:
        smai += 1
    else:
        smen += 1

print('''{} pessoas já atingiram a maioridade e {} pessoas ainda
são menores.'''.format(smai, smen))
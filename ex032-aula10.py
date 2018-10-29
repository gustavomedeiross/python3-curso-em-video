ano = int(input('What year is this?'))
ano = ano % 4
#leap = bissexto
if ano == 0:
    print('This year is leap!')
else:
    print('This year is not leap!')
s = int(input('Digite o seu salário!'))
if s > 1250:
    print('O seu novo salário é {}!'.format(s+s*0.1))
else:
    print('O seu novo salário é {}!'.format(s+s*0.15))
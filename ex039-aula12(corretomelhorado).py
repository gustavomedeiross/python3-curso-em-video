from datetime import date
sexo = str(input('Qual é o seu sexo? [M/F]')).upper().strip()[0]
while sexo not in 'MF':
    print('\033[31mSexo inválido. Tente novamente.\033[m')
    sexo = str(input('Qual é o seu sexo? [M/F]')).upper().strip()[0]
if sexo == 'F':
    print('Você não precisa se alistar.')
if sexo == 'M':
    print('Você foi/será obrigado a se alistar.')
    anodenascimento = int(input('Em que ano você nasceu?'))
    if date.today().year - anodenascimento > 18:
        print(f'Você já se alistou/deveria ter feito em {anodenascimento+18}')
    elif date.today().year - anodenascimento < 18:
        print(f'Você ainda deve se alistar, e será em {anodenascimento+18}')
    elif date.today().year - anodenascimento == 18:
        print('Você deve se alistar ESTE ANO!')
print('Obrigado por utilizar o programa!')
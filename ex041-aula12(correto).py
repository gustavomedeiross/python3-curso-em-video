from datetime import date
anodenascimeto = int(input('Ano de nascimento: '))
idade = date.today().year - anodenascimeto
print(f'O atleta tem {idade} anos')
if idade <= 9:
    print('Você é um atleta Mirim')
elif 9 < idade <= 14:
    print('Você é um atleta Infantil')
elif 14 < idade <= 19:
    print('Você é um atleta Junior')
elif 19 < idade <= 20:
    print('Você é um atleta Sênior')
else:
    print('Você é um atleta Master!')

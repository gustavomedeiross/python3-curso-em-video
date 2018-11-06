pessoa = {'Nome': str(input('Nome: ')), 'Média': float(input('Média: '))}
if pessoa['Média'] >= 7:
    pessoa['Situação'] = 'Aprovado'
else:
    pessoa['Situação'] = 'Reprovado'
for i, v in pessoa.items():
    print(f'{i} é igual a {v}')

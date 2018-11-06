from datetime import date
pessoa = {'nome': str(input('Nome: ')), 'nascimento': int(input('Ano de Nascimento: ')),
          'ctps': int(input('Carteira de Trabalho (0 não tem): '))}
idade = date.today().year - pessoa['nascimento']
if pessoa['ctps'] != 0:
    pessoa['contratação'] = int(input('Ano de contratação: '))
    pessoa['salário'] = float(input('Salário: R$:'))
    pessoa['aposentadoria'] = pessoa['contratação'] - pessoa['nascimento'] + 35
print('-=' * 30)
for k, v in pessoa.items():
    print(f'{k} tem o valor {v}')

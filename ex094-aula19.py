pessoa = {}
grupo = []
média = 0
while True:
    pessoa['nome'] = str(input('Nome: ')).capitalize()
    pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
    pessoa['idade'] = int(input('Idade: '))
    qrcnt = input('Quer continuar? [S/N] ').upper()[0]
    grupo.append(pessoa.copy())
    if qrcnt in 'Nn':
        break

for pos in range(0, len(grupo)):
    média += grupo[pos]['idade']

média = média/len(grupo)
print('-=' * 30)
print(f'- O grupo tem {len(grupo)} pessoas.')
print(f'- A média de idade é de {média:.2f} anos.')
print(f'- As mulheres cadastradas foram: ', end=' ')
for pos in range(0, len(grupo)):
    if grupo[pos]['sexo'] == 'F':
        print(grupo[pos]['nome'], end=' ')
print()
print('- Lista das pessoas que estão acima da média:')
for pos in range(0, len(grupo)):
    if grupo[pos]['idade'] > média:
        print(f'nome = {grupo[pos]["nome"]}; sexo = {grupo[pos]["sexo"]}; idade = {grupo[pos]["idade"]}.')
print('<< ENCERRADO >>')

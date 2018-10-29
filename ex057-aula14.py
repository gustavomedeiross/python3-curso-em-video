sexo = input('Informe o seu sexo. [M/F] =').upper().strip()[0]
while sexo not in 'MF':

    if sexo not in 'MFJ':
        print('Dados inválidos. Por favor, digite novamente.')
    if sexo == 'J':
        print('O que é isso? Você é um Jabuti?')
    sexo = str(input('Informe o seu sexo. [M/F] =')).upper()

if sexo == 'M':
    print('Você pertence ao sexo Masculino')
else:
    print('Você pertence ao sexo Feminino')
print('----FIM----')

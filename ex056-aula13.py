si = 0
maioridade = 0
ma20 = 0 #mulheres abaixo de 20 (quantidade)
for rdm in range(1, 5):
    print('===== {}ª PESSOA ====='.format(rdm))
    nome = input('Nome: ').strip()
    idade = int(input('Idade: '))
    sexo = input('[M/F]: ').upper()

    si += idade

    if sexo == 'M':
        if idade > maioridade:
            maioridade = idade
            nmi = nome #nome do homem de maior idade



    if sexo == 'F':
        if idade < 20:
            ma20 += 1

print('A média de idade do grupo é de {} anos.'.format(si/4))
print('O homem mais velho tem {} anos e se chama {}.'.format(maioridade, nmi))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(ma20))
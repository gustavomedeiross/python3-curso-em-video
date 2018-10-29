nome = input('Qual é o seu nome?')
nome = nome.title()
n1 = ('Silva' in nome)
if n1 == True:
    print('Você tem Silva no nome!')
if n1 == False:
    print('Você não tem Silva no nome!')

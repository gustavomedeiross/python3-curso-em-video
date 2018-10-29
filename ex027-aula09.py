nome = input('Digite o seu nome completo!')
nomex = nome.split()
n1 = len(nomex)
nome1 = nomex[0]
nome2 = nomex[n1-1]
print('O seu nome completo é = {}'.format(nome))
print('Primeiro nome = {}'.format(nome1))
print('Segundo nome = {}'.format(nome2))
import random
a1 = input('Escreva o nome do aluno 1!')
a2 = input('Escreva o nome do aluno 2!')
a3 = input('Escreva o nome do aluno 3!')
a4 = input('Escreva o nome do aluno 4!')
aluno = random.choice([a1, a2, a3, a4])
print('{}, apague o quadro!'.format(aluno))
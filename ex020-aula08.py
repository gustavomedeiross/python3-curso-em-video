import random
a1 = input('Aluno 1')
a2 = input('Aluno 2')
a3 = input('Aluno 3')
a4 = input('Aluno 4')
aluno = random.sample([a1, a2, a3, a4], k= 4)
print('A ordem de apresentação dos trabalhos será \n{}'.format(aluno))
#Crie um algoritmo que leia um número e diga o seu dobro, triplo e raiz quadrada.
from math import sqrt
n = int(input('Digite um número!'))
print('O dobro do número {} é {}, o triplo é {} e a raiz quadrada é {}!'.format(n, n*2, n*3, sqrt(n)))

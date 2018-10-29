from math import trunc
num = float(input('Type a number here!'))
print('The whole part of the number {}, is {}.'.format(num, trunc(num)))
#a diferença do truncate pro floor é que o floor SEMPRE vai arredondar pra baixo,
#mesmo quando o número for negativo. O trunc sempre arredondará para o mais próx de 0.
#exemplo: trunc(-2.87) = -2 //floor(-2.87) = -3.


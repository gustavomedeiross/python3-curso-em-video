import math
n1 = int(input('Digite um ângulo!'))
sen = math.sin(math.radians(n1))
cos = math.cos(math.radians(n1))
tan = math.tan(math.radians(n1))
print('O seno desse número é {}, o cosseno é {}, e a tangente é {}!'.format(sen, cos, tan))
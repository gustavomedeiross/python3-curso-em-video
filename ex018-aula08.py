import math
n1 = int(input('Digite um ângulo!'))
sen = math.sin(math.radians(n1))
cos = math.cos(math.radians(n1))
tan = math.tan(math.radians(n1))
print('O seno desse número é {:.2f}, o cosseno é {:.2f}, e a tangente é {:.2f}!'.format(sen, cos, tan))

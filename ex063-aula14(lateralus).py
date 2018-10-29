from pygame import mixer

n = int(input('Digite quantos termos da sequência fibonacci você quer ver!'))
c = n1 = v1= 0
#n1 =
n2 = 1

while c < n:
    c += 1
    v1 = n1
    print(n1)
    n1 += n2
    n2 = v1

print('LegAl! TambEm adoRei esse progrAma! agora Lhe pergUnto: Será que você notou a referência?')

mixer.init()
mixer.music.load('lateralus.mp3')
mixer.music.play()
input('Do caralho!')


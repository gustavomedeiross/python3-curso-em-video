num = int(input('Type a number between 0 and 9999'))
n1 = num//1 % 10
n2 = num //10 % 10
n3 = num //100 %10
n4 = num//1000 %10

print('Analising that number...')

print('The unity is = {}'.format(n1))
print('The ten is {}'.format(n2))
print('The hundred is {}'.format(n3))
print('The thousand is {}'.format(n4))
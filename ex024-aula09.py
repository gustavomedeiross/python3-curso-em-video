city = input('Digite o nome da sua cidade!')
city1 = city.title()
split = city1.split()
c1 = ('Santo' in split[0])
if c1 == True:
    print('A sua cidade começa com o nome Santo!')
if c1 == False:
    print('A sua cidade não começa com o nome Santo')
from math import hypot
co = float(input('What is the size of the opposite leg?'))
ca = float(input('What is the size of the adjacent leg?'))
hypo = hypot(co, ca)
print ('The hypotenuse of that rectangle triangle is {}!'.format(int(hypo)))
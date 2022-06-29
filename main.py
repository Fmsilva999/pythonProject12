
a = float(input('primeiro seguimento: '))
b = float(input('segundo seguimento: '))
c = float(input('terceiro seguimento: '))

if a == b == c:
    tri = 'EQUILÁTERO'
elif a == b != c or b == c != a or a == c != b:
    tri = 'ISÓSCELES'
else :
    tri = 'ESCALENO'

if a + b > c and b + c > a and a + c > b:
    print('os seguimentos acima podem forma um triagulo {}'.format(tri))
else:
    print('os seguimentos acima não podem formar um triagulo')
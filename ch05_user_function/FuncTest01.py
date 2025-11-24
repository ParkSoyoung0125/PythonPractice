def func01(a,b = 5):
    return (2*a) + (3*b)

a = 5
b = 10
print('func01(%d,%d) = %d' % (a,b,func01(a,b)))

print('func01(%d,%d) = %d' % (4,7,func01(4,7)))

print('func01(%d) = %d' % (10, func01(10)))
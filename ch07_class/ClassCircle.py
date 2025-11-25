class Circle:
    type = '원'
    def __init__(self, b,c, radius):
        self.b = b
        self.c = c
        self.radius = radius

    def showinfo(self):
        print('원 중심 : %d, %d' % (self.b,self.c))
        print('반지름 : %d' % (self.radius))
        print('면적 : %.2f' % (self.radius*self.radius*3.14))

print('도형의 타입 : %s' % (Circle.type))

print('-' * 20)
circle1 = Circle(3, 5, 10)
circle1.showinfo()
print( '-' * 20 )
circle2 = Circle(8, 6, 20)
circle2.showinfo()
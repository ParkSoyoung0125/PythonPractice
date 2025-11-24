def namePrint():
    name = input('이름 :')
    age = int(input('나이 :'))
    print('이름 : %s, 나이 : %d' % (name, age))

def sayhello(message, cnt):
    for i in range(cnt):
        print(message)
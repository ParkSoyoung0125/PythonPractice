def sayhello(message, n=10):
    for i in range(n):
        print(f'{message}')

sayhello('안녕하세요',5)
sayhello('방가')
sayhello(message='Hi')
sayhello(message='Hi', n = 3)
sayhello(n = 3, message='Hi')


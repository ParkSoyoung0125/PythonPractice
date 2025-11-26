print('파일에 기록합니다.')

filename = 'mem.txt'
myfile01 = open(file=filename, mode='wt', encoding='utf-8')
print(type(myfile01))

members = ['홍영식','김민수','박진철','강호숙']

for mem in members:
    message = f'{mem}님 안녕하세요\n'
    myfile01.write(message)

myfile01.close() # 메모리에 있는 파일을 하드디스크에 저장하려면 file.close()를 해줘야함

print(f'{filename} 파일이 생성됨')

print(f'기존 파일 {filename}에 내용을 더 추가합니다.')
myfile02 = open(file=filename, mode='wt', encoding='utf-8')

for idx in range(len(members)):
    if idx % 2 == 0:
        message = f'{idx}번째 고객 {members[idx]}님 반갑습니다.\n'
    else:
        message = f'{idx}번째 고객 {members[idx]}님 어서오세요.\n'
    #end if
    myfile02.write(message)
#end for
myfile02.close()

print('반복문을 사용하여 파일 여러개를 생성합니다.')
print('파일 이름 : somefile01.txt ~ somefile10.txt')

for idx in range(1,11):
    filename = 'somefile'+ str(idx).zfill(2)+'.txt'
    myfile03 = open(filename,mode='wt', encoding='utf-8')

    message = '파일 생성 테스트' + str(idx)
    myfile03.write(message)
    myfile03.close()

    print(f'{filename} 파일 생성됨')

print('다음 멤버들의 이름을 사용한 파일을 만들어보세요.')
members = ['홍영식','김민수','박진철','강호숙']

for idx in members:
    filename = idx+'.txt'
    file = open(filename, mode='wt',encoding='utf-8')

    file.write(idx + '고객용 텍스트 파일\n')
    file.close()
    print(idx +' 파일 생성됨.')
#end for

print('with 구문을 사용하면, 암시적으로 close() 함수가 호출됨.')
with open(file='test.txt', mode='wt',encoding='utf-8') as testfile:
    testfile.write('가나다\n')
    testfile.write('abc\n')
    testfile.write('123\n')

    print('hello world', file=testfile)
#end with

# def print(self, *args, sep=' ', end='\n', file=None):
# 내장함수 print의 file 기본값은 none -> 모니터에 출력됨
# 이 file에 파일을 지정하면 그 파일에 출력함.
name = '김철수'
age = 30
height = 175.3456789
address = '마포'

print('이름 : %s' % (name))
print('나이 : %d' % (age))
print('키(1) : %f' % (height)) # 실수의 기본값은 소수점 6자리까지 표현
print('키(2) : %.3f' % (height))
print('키(2) : [%10.4f]' % (height)) #전체 10자리를 확보하되, 소수점 4자리까지
print('주소 : %s' % (address))

message = '이름은 %s이고, 나이는 %d살입니다.'
print(message % (name, age)) # 열거한 순서대로 할당됨.

su01 = 3
su02 = 5
message = '%d 더하기 %d는 %d입니다.'
print(message % (su01, su02, (su01+su02)))

a = 2
b = 10
# pow(a,b) : a의 b제곱을 해주는 내장함수
print('%d의 %d승은 %d입니다.' % (a, b, pow(a,b)))
# 2의 10승은 1024입니다.

hello = '안녕'
message = '[%10s]' % hello
print(message)

message = '[%-10s]' % hello
print(message)
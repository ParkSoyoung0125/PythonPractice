# print('이름 입력 : ', end='')
# name = input()
#
# age = int(input('나이 입력 : '))
#
# print('\n% 포맷 코드 형식으로 출력')
# print('이름 : %s' % name)
# print('나이 : %s' % age)
#
# print('\nformat() 함수를 사용한 출력')
# message = '제 이름은 {}이고, 나이는 {}세입니다.'
# print(message.format(name, age))

a = input('숫자 1 입력 : ')
b = input('숫자 2 입력 : ')
message = '{} 곱하기 {}는 {}'
print(message.format(a,b,a+b))
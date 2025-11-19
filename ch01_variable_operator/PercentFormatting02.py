# 다음 변수를 사용하여 출력결과처럼 출력해보세요
# 내장함수 pow(a,b)는 a의 b제곱입니다.

'''
[출력결과]
김철수이(가) 사과를 8개 먹었습니다.
 4 곱하기 9는 36입니다.
 2.000000의 3.000000 제곱은 8.000000입니다.
 %를 표현하려면 %%를 표시해야 합니다.
비율 : 45.670000%
'''

name = '김철수'
fruit = '사과'
gaesu = 8
su01 = 4
su02 = 9
su03 = -5
a = 2.0
b = 3.0
rate = 0.4567
message = '%s이(가) %s를 %d개 먹었습니다.'
print(message % (name, fruit, gaesu))

message = '%d 곱하기 %d는 %d입니다.'
print(message % (su01, su02, (su01*su02)))

message = '%d의 절댓값은 %d입니다.'
print(message % (su03,abs(su03)))

message = '%.6f의 %.6f 제곱은 %.6f입니다.'
print(message % (a, b, pow(a,b)))

print('%s를 표현하려면 %s를 표시해야합니다.' % ('%','%%'))

print('비율 : %10.6f%%' % (rate*100))
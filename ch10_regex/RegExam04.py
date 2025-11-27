import re

from ch10_regex.RegExam03 import mystring01

print('(1) split 함수 : 정규식 패턴을 사용하여 문자열을 분리')
mystring01 = '아메리카노, 카페라떼:카푸치노 모카'
regEx = '[z :]'
pattern = re.compile(regEx)
result = pattern.split(mystring01)
print(result)

print('\n(2) sub 함수 : 패턴과 일치하는 문자열을 대체(substitute)함.')
print('하이픈(-)을 슬래시(/)로 대체함')
mystring02 = '커피 생산일 : 2025-11-27'
regEx = '-'
pattern = re.compile(regEx)
result = pattern.sub('/',mystring02) # sub(바뀔 문자열, 문자열대상)
print(result)


print('\n(3) subn 함수 : 패턴과 일치하는 문자열을 n개만 대체(substitute)함.')
mystring03 = '01-02-03-04-05'
regEx = '-'
pattern = re.compile(regEx)

print(f'원본 문자열 : {mystring03}')
for idx in range(1,5):
    result = pattern.subn('/',mystring03,count=idx)
    print(f'count = {idx} → {result}')

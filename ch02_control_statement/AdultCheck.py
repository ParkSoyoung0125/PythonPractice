name = input('이름 입력 : ')
age = int(input('나이 입력 : '))

# 변수 앞에 언더바를 붙여서 내부적으로 사용하는 보조변수
_gender = int(input('성별 입력(숫자 1, 2, 3, 4 중 택1) : '))

# 최종적으로 의미를 가지는 변수
gender = '남자'

if (age >= 18):
    adult = '성인'
else :
    adult = '성인'
#end if

if(_gender == 1 or _gender == 3):
    gender
else :
    gender = '여자'

print('%s는 %s이고, %s 입니다.' % (name,adult,gender));
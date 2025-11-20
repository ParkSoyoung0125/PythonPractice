name = input('이름 입력 : ')
kor = int(input('국어 점수 입력 : '))
eng = int(input('영어 점수 입력 : '))
math = int(input('수학 점수 입력 : '))

score = kor + eng + math

avg = score / 3.0

if avg >= 90:
    hakjum = 'A'
    comment = 'Excellent'
elif avg >= 80:
    hakjum = 'B'
    comment = 'Good'
elif avg >= 70:
    hakjum = 'C'
    comment = 'Not bad'
elif avg >= 60:
    hakjum = 'D'
    comment = 'So bad'
else:
    hakjum = 'F'
    comment = 'Retry'
#end if

print('%s님의 정보\n국어 : %d, 영어 : %d, 수학 : %d' % (name, kor, eng, math))
print('총점 :  %d' % score)
print('평균 :  %4.2f' % avg)
print('학점 : %s' % hakjum)
print('코멘트 : %s' % comment)
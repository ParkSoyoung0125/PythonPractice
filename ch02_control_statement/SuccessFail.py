mid = int(input('중간고사 점수 : '))
fin = int(input('기말고사 점수 : '))

score = (mid * 0.4) + (fin*0.6)

if score >= 70:
    result = '합격'
else: result = '불합격'

print('중간고사 점수 : %d ' % mid)
print('기말고사 점수 : %d' % fin)
print('총점 : %4.1f' % score)
print('합격여부 : %s' % result)
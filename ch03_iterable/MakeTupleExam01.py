#Tuple
coffee01 = ('아메리카노','카페라떼')
coffee02 = ('콜드브루','아이스커피')
# 소괄호 없이 콤마로 연결하면 무조건 Tuple
coffee03 = ('카푸치노','마끼야또')

print('자료형 타입 : ', end=' ')
print(type(coffee01)) # 자료형 알려주는 명령어

mylist = ['바닐라라떼','플랫화이트']
coffee04 = tuple(mylist)

# +를 사용하여 기존 요소에 새로운 요소 추가 가능
coffees = coffee01 + coffee02 + coffee03 + coffee04 + ('에스프레소',)

length = len(coffees)
print('요소 개수 : %d' % length)
print(coffees)

# 1번째 요소를 '고구마라떼'로 변경
#coffees[1] = '고구마라떼' <- Tuple은 쓰기작업 불가능.
# 편집 없이 빠른속도로 구동하려면 Tuple, 편집하려면 list

# 인덱싱
print('앞에서 1번째 요소 : %s' % coffees[0])
print('뒤에서 1번째 요소 : %s' % coffees[-1])

# 슬라이싱
# coffees[start:end:step] : start부터 시작하여 end 직전까지 step씩 슬라이싱
print('1번째~3번째까지의 요소 : ')
print(coffees[1:4]) # 0,1,2 -> 1,2,3번째
print('3번째 이후의 요소 : ')
print(coffees[3:]) # [3:] => 4번째부터
print('0번째~3번째 이전까지의 요소 : ')
print(coffees[:3])

print('홀수 요소 : ')
print(coffees[0::2]) # 0부터 끝까지 2칸씩 건너뛰기 = 홀수
print('짝수 요소 : ')
print(coffees[1::2]) # 1부터 끝까지 2칸씩 건너뛰기 = 짝수
print('전부 출력 : ')
print(coffees[::])

mycount = coffees.count('아메리카노')
print('아메리카노의 개수 : %d' % mycount)

myindex = coffees.index('콜드브루')
print('콜드브루의 인덱스 번호 : %d' % myindex)
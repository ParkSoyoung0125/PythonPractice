coffees = [] #empty list
coffees = list() # 내장 함수를 이용한 empty list 생성

coffees.append('아메리카노')
coffees.append('콜드브루')
coffees.append('카푸치노')
coffees.append('바닐라라떼')
coffees.append('디카페인아메리카노')
coffees.append('카페라떼')

count = len(coffees)
print('요소 개수 : %d' % count)

# 인덱싱
print('앞에서 1번째 요소 : %s' % coffees[0])
print('뒤에서 1번째 요소 : %s' % coffees[-1])

# 슬라이싱
# coffees[start:end:step] : start부터 시작하여 end 직전까지 step씩 슬라이싱
print('1번째~3번째까지의 요소 : %s' % coffees[1:4]) # 1,2, 3 -> 2,3,4번째
print('3번째 이후의 요소 : %s' % coffees[3:]) # [3:] => 4번째부터
print('0번째~3번째 이전까지의 요소 : %s' % coffees[:3])

coffees[1] = '고구마라떼' #해당 자리에 덮어쓰기 가능

print('홀수 요소 : %s' % coffees[0::2]) # 0부터 끝까지 2칸씩 건너뛰기 = 홀수
print('짝수 요소 : %s' % coffees[1::2]) # 1부터 끝까지 2칸씩 건너뛰기 = 짝수
print('전부 출력 : %s' % coffees[::])

print('오름차순 정렬')
coffees.sort()
print(coffees)

print('내림차순 정렬')
coffees.sort(reverse=True)
print(coffees)
coffees = set()

coffees.add('아메리카노')
coffees.add(100)
coffees.add(True)
coffees.add('아메리카노') # set은 중복 제거

coffees.clear()

coffees.add('아메리카노')
coffees.add('에스프레소')
coffees.add('믹스커피')
coffees.add('카페라떼')

newItem = ['콜드브루','고구마라떼','디카페인커피']
coffees.update(newItem)

# 집합은 순서가 없어서 인덱싱이 불가능함
# print(coffees[3])

findItem = '카푸치노'
boolean = findItem in coffees
print(f'{findItem} 존재 여부 : {boolean}') #fstring

findItem = '마키아또'
if not findItem in coffees:
    coffees.add(findItem)

findItem = '믹스커피'
coffees.remove(findItem)

try:
    findItem = '바닐라라떼'
    coffees.remove(findItem)
except KeyError:
    print(f'{findItem}은 목록에 존재하지 않습니다.')
#end try

#discard 메소드는 존재하지 않더라도 예외없이 넘어감
coffees.discard('바닐라라떼')

# 집합은 순서가 없으므로, 어떤 데이터가 나올지 예측할 수 없음
popItem = coffees.pop()
print('pop()으로 제거된 요소 : ', popItem)

print('반복문을 사용한 출력')
for element in coffees:
    print(element)
#end for

print('자료형 타입 : ', end=' ')
print(type(coffees))
print('요소 개수 : %d' % len(coffees))
print(coffees)

print('집합 연산')
beverage01 = set(['고구마라떼','에스프레소','아메리카노','마끼아또'])
beverage02 = set(['아메리카노','마끼아또','카페라떼','디카페인커피'])

union_set = beverage01.union(beverage02) # 합집합/중복제거
print(f'합집합 : {union_set}')

union_set = beverage01 | beverage02 # | 기호로도 union 가능
print(f'합집합 : {union_set}')

difference_set01 = beverage01.difference(beverage02) # 차집합(beverage01 - beverage02)
print(f'차집합01 : {difference_set01}')

difference_set02 = beverage02 - beverage01 # 차집합(beverage02 - beverage01) / - 기호로도 가능
print(f'차집합02 : {difference_set02}')

intersection_set = beverage01.intersection(beverage02) # 교집합
print(f'교집합 : {intersection_set}')

# 차집합들의 합집합 = 교집합 뺀 나머지
symmetric_difference_set01 = beverage01.symmetric_difference(beverage02)
print(f'차집합들의 합집합 : {symmetric_difference_set01}')

symmetric_difference_set02 = beverage01^beverage02
print(f'차집합들의 합집합 : {symmetric_difference_set02}')

print('부분 집합')
super_set = set(['고구마라떼','에스프레소','아메리카노','마끼아또'])
sup_set_01 = set(['아메리카노','마끼아또'])
sup_set_02 = set(['바닐라라떼','마끼아또'])

boolean = sup_set_01.issubset(super_set)
if boolean:
    print(f'{sup_set_01}은 {super_set}의 부분 집합입니다.')
else:
    print(f'{sup_set_01}은 {super_set}의 부분 집합이 아닙니다.')
#end if

boolean = sup_set_02.issubset(super_set)
if boolean:
    print(f'{sup_set_02}은 {super_set}의 부분 집합입니다.')
else:
    print(f'{sup_set_02}은 {super_set}의 부분 집합이 아닙니다.')
#end if

boolean = super_set.issubset(sup_set_01)
if boolean:
    print(f'{super_set}은 {sup_set_01}의 부분 집합입니다.')
else:
    print(f'{super_set}은 {sup_set_01}의 부분 집합이 아닙니다.')
#end if
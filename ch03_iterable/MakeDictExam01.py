from warnings import catch_warnings

coffees = dict() # {} 기호도 가능

coffees['에스프레소'] = 1000 # dict 안에 신규품목 추가

coffees['에스프레소'] = 1500 # 이미 존재하면 덮어쓰기
coffees['카페라떼'] = 2000
coffees['카푸치노'] = 3000
coffees['마끼야또'] = 4000

findData = '카페라떼'
boolean = findData in coffees

if boolean:
    print('키 \'%s\'이(가) 존재합니다.' % findData)
else:
    print('키 %s이(가) 존재하지 않습니다.' % findData)

findData = '핫초코'
boolean = findData in coffees

if not boolean:
    print('키 %s이(가) 존재하지 않기 때문에 추가합니다.' % findData)
    coffees[findData] = 5000
    print(coffees)
else:
    print('키 \'%s\'이(가) 존재합니다.' % findData)
# end if

print('키(key) 목록 : ', coffees.keys())
print('값(value) 목록 : ', coffees.values())

price = 6000
boolean = price in coffees.values()

if boolean:
    print('단가 \'%d\'짜리 품목이 존재합니다.' % price)
else:
    print('단가 \'%d\'짜리 품목이 존재하지 않습니다.' % price)
    coffees['아이스커피'] = price
#end if

listCoffee = ['바닐라라떼','라벤더밀크티','딸기라떼','콜드브루'] # list는 순서 있음
for idx in range(len(listCoffee)):
    coffees[listCoffee[idx]] = (idx+7)*1000
    print(coffees)
# end for

findData = '핫초코'
print('%s의 가격은 %d입니다.' % (findData, coffees[findData]))

targetList = ['라벤더밀크티','밀크커피']
for key in targetList:
    try:
        message = '품명 : %s, 가격 : %d' % (key, coffees[key])
        print(message)
    except KeyError:
        print('%s은(는) 존재하지 않아서 새로 추가합니다.' % key)
        coffees[key] = 5000
    #end try
#end for

findData = '둥굴레차'
price = coffees.get(findData,3000) # 없으면 기본 값으로 대체 / 뒤에 설정한 값이 디폴트 값이 됨.
print('품명 : %s, 가격 : %d' % (findData, price))

findData = '아이스커피'
popItem = coffees.pop(findData) # 목록에서 해당 항목이 삭제되면서 좌변 변수에 해당 항목의 value을 리턴
print('삭제된 품목 %s의 가격은 %d원이었습니다.' % (findData, popItem))

del coffees['에스프레소'] # '에스프레소' 항목 삭제

for (key, value) in coffees.items():
    message = '품목 %s의 단가는 %d원 입니다.' % (key, value)
    print(message)
#end for

# 전체 목록 출력
#단, '카페라떼'와 '카푸치노'는 500원 인상
# '핫초코'는 500원 인하
print('전체 목록 출력')
for key in coffees.keys():
    if key == '카페라떼' or key == '카푸치노':
        coffees[key] += 500
    elif key == '핫초코':
        coffees[key] -= 500
    else:               # 파이썬은 else에 아무것도 안넣으면 자바와 다르게 에러가 남, 뭐라도 적던지 else를 아예 빼야 함.
        pass            # 통과시킨다는 뜻
    #end if
    message = '품명 : %s, 가격 : %d' % (key, coffees[key])
    print(message)
#end for

coffees.clear() # 원소 다 지우기

if len(coffees) == 0:
    print('my dictionary is empty')
else:
    print('my dictionary is not empty')

print(type(coffees))
print('요소 개수 : %d' % len(coffees))
print(coffees)
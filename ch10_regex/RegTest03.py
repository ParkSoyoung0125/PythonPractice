import re

print('findall 함수는 정규식과 매치되는 모든 문자열을 list 형식으로 반환해 줍니다.')
order_info = '오늘 커피가격은 아메리카노 3500원, 라테 4200원, 모카 4800원입니다.'

# 날짜처럼 예시를 맞추기 위해 0000/00/00 형태로 출력하는 형식 유지
# 이번에는 가격을 "3500/4200/4800" 형태로 출력
regEx = '\d+'
pattern = re.compile(regEx)
result = pattern.findall(order_info)
mymatch = f'{result[0]}/{result[1]}/{result[2]}'
print(mymatch)



total = 0
print('\n총 주문 수량 구하기')
order_qty = '아메리카노 2잔, 카페라테 3잔, 바닐라라테 1잔 주세요.'
regEx = '\d+'
pattern = re.compile(regEx)
result = pattern.findall(order_qty)
total = int(result[0])+int(result[1])+int(result[2])
print('총 주문 수량 : %d' % total)


print('\nb로 시작하는 커피 메뉴만 추출하여 정렬하기')
menu_list = '브루잉 brew 블랙 black 바닐라 vanilla 바닐라라테 latte 블루 blue'
regEx = 'b[a-z]*'
pattern = re.compile(regEx)
result = pattern.findall(menu_list)
print(result)


print('\nfinditer 함수는 결과물을 반복 가능한 객체 형식으로 반환해 줍니다.')
print('일반적으로 for 구문과 같이 사용됩니다.')


print('\n커피 주문 수량 계산(finditer)')
mycoffee = '에스프레소 1잔, 아메리카노 2잔, 카푸치노 3잔'
total = 0
regEx = '\d+'
pattern = re.compile(regEx)
result = pattern.finditer(mycoffee)
for item in result:
    start, end = item.start(), item.end()
    print(f'문자열 위치 : {item.span()}')
    print(f'해당 문자열 : {item.group()}')
    print(f'문자열 시작 위치 : {item.start()}')
    print(f'문자열 끝 위치 : {item.end()}')
    total += int(item.group())

print('음료 총 주문 수량 : %d' % total)



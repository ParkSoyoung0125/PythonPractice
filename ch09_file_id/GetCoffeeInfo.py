# CoffeeCheck.py
myencoding = 'UTF-8'

# 읽어올 파일
source = open(file='coffee.txt', mode='rt', encoding=myencoding)

# 신규 생성할 파일
write_file = 'coffee_result.txt'
destination = open(file=write_file, mode='wt', encoding=myencoding)

discounts = {
    "아메리카노": 0.10,   # 10% 할인
    "라떼": 0.05,         # 5% 할인
    "카푸치노": 0.07,     # 7% 할인
    "바닐라라떼": 0.08,   # 8% 할인
    #"모카": 0.06          # 6% 할인
}

# 파일 내용 읽어서 리스트로 변환
data = [item.strip() for item in source.readlines()]
print(data)

for line in data:
    coffee = line.split(',')  # 상품명, 가격, 재고
    # print(coffee)

    name = coffee[0]
    price = int(coffee[1])
    stock = int(coffee[2])

    total_value = price * stock * (1.0 - discounts.get(name , 0.06))  # 총 재고 금액
    total_value = int(total_value)

    # '상품명/가격/재고/총재고금액' 형식
    result_line = f'{name}/{price}/{stock}/{total_value}\n'
    print(result_line)

    destination.write(result_line)

source.close()
destination.close()

print(f'{write_file} 파일 생성 완료')

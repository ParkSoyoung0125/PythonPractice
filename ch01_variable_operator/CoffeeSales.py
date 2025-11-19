coffee = 3
price = 2000

# 기호 {} : format placeholder 또는 format field
message = '우리 매장에는 커피 {}잔이 판매 가능합니다.'
print(message.format(coffee))

message = f'우리 매장에는 커피 {coffee}잔이 판매 가능합니다.'
print(message)

message = '우리 매장 커피 1잔 가격은 {}원입니다.'
print(message.format(price))

message = '우리 매장 커피 {}잔 가격은 {}원입니다.'
print(message.format(coffee, price*coffee))

message = '커피 {}잔, 단가 : {}'
print(message.format(coffee, coffee*price))
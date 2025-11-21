fruits = ['사과','감','오렌지','한라봉','바나나']

for (idx,value) in enumerate(fruits):
    message = '%d번째 품목은 \'%s\'입니다.' % (idx+1,value)
    print(message)
#end for
print('-'*30)

for (idx,value) in enumerate(fruits, start=1):
    message = '%d번째 품목은 \'%s\'입니다.' % (idx,value)
    print(message)
#end for
print('-'*30)

for item in enumerate(fruits):
    message = '%d번째 품목은 \'%s\'입니다.' % (item[0],item[1])
    print(message)
#end for
print('-'*30)

for item in enumerate(fruits):
    message = '{}번째 값 : {}'.format(item[0],item[1])
    print(message)
#end for
print('-'*30)

print('*기호는 가변 매개 변수로 인식되며, 내부에서 tuple로 처리됨.') # 가변 매개변수 : 변경 가능한 매개 변수
for item in enumerate(fruits):
    # message = '{}번째 값 : {}'.format(item[0],item[1])
    message = '{}번째 값 : {}'.format(*item)
    print(message)
#end for
print('-'*30)

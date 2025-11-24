# 함수의 정의
# 매개 변수 = parameter, argument, 인자, 인수라고 부르기도 함.
def add(a,b=15):
    return a+b
#end def

su01 = 14
su02 = 5

# positional argument : index를 이용하여 매개 변수에 할당하는 방식
add1 = add(su01,su02) # 함수 호출
print('%d + %d = %d' % (su01, su02, add1))

print('%d + %d = %d' % (100, 200, add(100,200)))

# keyword argument : 매개 변수 키워드를 이용하여 매개변수에 할당하는 방식
add1 = add(b = su01, a=su02)
print('%d + %d = %d' % (su02, su01, add1))

# 2방식의 혼합(positional 방식 + keyword 방식 혼합)
add1 = add(15, b=su02)
print('%d + %d = %d' % (15, 20, add1))

# 위치기반 인자이기 때문에 매개변수를 누락하면 에러가 남.
# TypeError: add() missing 1 required positional argument: 'b'
# 함수 생성 시 기본값을 설정하면 매개변수 안넣어도 오류가 안남 / def add(a,b=15)
# 자바와 달리 기본값 할당이 가능하기 때문에 오버로딩 개념이 없음.

result = add(10)
print(result) # result = 25

# 단, 인자가 2개 이상일 경우 첫번째 인자에 기본값을 할당하면, 두번째 인자도 기본값을 할당해줘야 하지만,
# def add(a, *, b)처럼 가운데 *를 주면 첫번째 인자에만 값 할당이 가능함


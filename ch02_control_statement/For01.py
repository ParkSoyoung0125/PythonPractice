total = 0
for i in range(97,1,-5):
    total += i
#end for
print('총합01 : %d' % total)

# 1 ~ 100까지 3씩 증가하는 수의 총합
total = 0
for i in range(1,101,3):
    total += i
#end for

print('총합02 : %d' % total)

#97 ~ 2까지 5씩 감소하는 수의 총합
total = 0
for i in range(97,1,-5):
    total += i
#end for

print('총합01 : %d' % total)

#1 ~ 96까지 5씩 증가하는 수의 제곱합
total = 0
for i in range(1,97,5):
    total += i**2 # i의 2제곱 / i**0.5는 루트
#end for

print('총합01 : %d' % total)

#1*2 + 2*3 + 3*4 + ... + 5*6
total = 0
for i in range(1,6):
    total += i*(i+1)
#end for

print('총합01 : %d' % total)
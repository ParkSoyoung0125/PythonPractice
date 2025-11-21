#다음 리스트의 모든 요소들을 반복문을 사용하여 총합을 구해 보되, range 함수를 사용하는 방식과 사용하지 않는 두 가지 방식을 사용하여 풀어 보세요.
#단, 요소의 값이 음수인 항목은 절대 값으로 변경하여야 합니다.
mylist = [10, -20, 30, -40, 50]
total = 0;
for i in mylist:
    total += abs(i)
print(total)

total = 0
for i in range(len(mylist)):
    total += abs(mylist[i])
print(total)
#sum 집계 함수를 이용하여 다시 풀어 보세요.
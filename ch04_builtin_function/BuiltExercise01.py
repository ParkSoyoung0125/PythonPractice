coffees = ['아메리카노','카페라떼','에스프레소']
price = [1000,2000,3000,4000]

#zip()
for item in zip(coffees, price): # 가장 적은 원소에 맞춰서 뒷부분은 날라감 => price의 4000은 날아간다는 뜻
    print(item)
#end for

# sorted
mycoffeelist = dict(zip(coffees, price))
print(mycoffeelist)

print('key를 사용한 오름차순 정렬')
result1 = sorted(mycoffeelist.keys())
print(result1)

print('key를 사용한 내림차순 정렬')
result2 = sorted(mycoffeelist.keys(), reverse=True)
print(result2)

print('value를 사용한 오름차순 정렬')
result3 = sorted(mycoffeelist.values())
print(result3)

print('value를 사용한 내림차순 정렬')
result4 = sorted(mycoffeelist.values(), reverse=True)
print(result4)

#다음 리스트를 사용하여 물음에 답해 보세요.
human = ['김철수', '홍길동', '박영희']
jumsu = [50, 60, 70]

#zip() 함수를 사용하여, 다음과 같은 데이터 mylist를 만드세요.
# mylist = [('김철수', 50), ('홍길동', 60), ('박영희', 70)]

mylist = list(zip(human, jumsu))
print(mylist)

#mylist를 사전 mydict으로 변경해 보세요.(dict() 함수 적절히 사용)
mydict = dict(zip(human, jumsu))
print(mydict)

#mydict를 이용하여 점수가 높은 사람 순부터 '이름'을 출력해 보세요.(sorted() 함수)
for i in sorted(mydict,key=mydict.get, reverse=True): # mydict:정렬대상, key:정렬기준(key로 가져온 '값'), reverse=True :내림차순
    print(i)
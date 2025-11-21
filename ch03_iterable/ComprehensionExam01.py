mylist01 = [idx for idx in range(1,5)]
print(mylist01)

mylist02 = [idx*10 for idx in range(1,6)]
print(mylist02)

mylist03 = [idx for idx in range(1,101,3)]
print(mylist03)

mylist04 = [idx for idx in range(1,101,3) if idx % 10 == 0]
print(mylist04)

exam_jumsu = [75, 30, 85, 50] # 합격 기준은 60점 이상
mylist05 = [grade for grade in exam_jumsu if grade >= 60]
print(mylist05)

# 다음 항목들을 이용하여 사전으로 만들어 보기
# 아래 fruits는 튜플 요소 3개를 담고 있는 리스트임
fruits = [('바나나',10),('사과',20),('오렌지',30)]

#dict comprehension
mydict01 = {item[0]:item[1] for item in fruits} # 0번째 요소가 key, 1번째 요소가 value가 된다는 뜻
print(mydict01)

# 학생들의 시험 점수를 사전으로 만들어 보세요.
# {'이문식': (80, 90, 50), '강수현':  (50, 60, 80), '윤정혁': (70, 40, 60)}
students = [
    ('이문식', 80, 90, 50),
    ('강수현', 50, 60, 80),
    ('윤정혁', 70, 40, 60)
    ]
mydict02 = {one[0]:one[1:] for one in students} # one[0] = key, one[1:] = 1번째 자리부터 슬라이싱 해서 value에 담기
print(mydict02)

# 점수들의 총합을 사전의 value로 만들어 보세요.
# sum 함수는 파이썬 내장 함수 중의 하나
# {'이문식': 220, '강수현': 190, '윤정혁': 170}
mydict03 = {one[0]:sum(one[1:]) for one in students}
print(mydict03)
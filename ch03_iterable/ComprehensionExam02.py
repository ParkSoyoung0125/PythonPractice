# list comprehension을 활용한 문제
# 평균 이상 점수를 받은 학생 수 출력하기
scores = [55, 80, 92, 45, 68, 88]  # 평균 이상이면 '우수'
avg = sum(scores) / len(scores)

overavg = len([idx for idx in scores if idx >= avg])
print(f'평균 점수 : {avg}, 평균을 넘은 학생 수 : {overavg}')

# 나이가 18세 이상인 사람만 추출하여 몇 명인지 출력
ages = [12, 17, 18, 20, 35, 15]

overage = len([idx for idx in ages if idx >= 18])
print(f'{ages} 중 18세 이상인 사람의 수 : {overage}')

# 양수만 골라서 개수 출력하기
numbers = [-5, 3, 0, 7, -2, 10, -8]
num = len([idx for idx in numbers if idx > 0])
print(f'{numbers} 중에서 양수인 수의 개수 : {num}')

# 짝수만 골라서 출력 및 개수 표시
data = [1, 4, 7, 10, 13, 16]

odd = [o for o in data if o % 2 == 0]
odd1 = len([o for o in data if o % 2 == 0])
print(f'짝수인 수 : {odd}, 짝수 갯수 : {odd1}')

# 이름 리스트에서 3글자 이상인 이름만 추출
names = ["유나", "철수", "민지", "Tom", "Ann", "Jennifer"]

namelist = [n for n in names if len(n) >= 3]
print(f'이름이 3글자 이상이 사람의 이름 : {namelist}')
# 랜덤 정수 생성 연습
# random.randint()를 사용하여
# 1~100 사이 랜덤 정수를 10개 리스트에 저장한 뒤 출력해 보세요.
# 동일한 숫자가 여러 번 나올수도 있습니다.
import random

randNumbers = [random.randint(1, 100) for n in range(10)]
print('1~100 사이의 정수 10개 : ', randNumbers)


# 메뉴 랜덤 추천하기
# 다음 메뉴 중에서 오늘 점심 메뉴를 1개 추천하세요.
menu = ['김치찌개', '제육볶음', '돈까스', '파스타', '떡볶이', '초밥', '김밥']
randMenu = random.choice(menu)
print('오늘의 랜덤 메뉴 : ',randMenu)


# 순서 섞기(shuffle)
# 다음 학생들의 시험 발표 순서를 무작위로 정해 보세요.
students = ['민수', '지우', '하은', '준서', '다현', '서준', '유진']
random.shuffle(students)
for i in students:
    print(i)


# 무작위 표본 추출(sample)
# 다음 회사의 직원 목록에서 랜덤하게 4명만 뽑아 프로젝트 TF팀을 만들어 보세요.
employee = ['홍길동','김철수','이영희','박민지','최현우','송다인','정윤호','백지현']
def randemployees():
    random.shuffle(employee)
    team = employee[0:4]
    return team

for i in range(0,len(employee),4):
    teams = randemployees();
    print(teams)

# 아래 학생 리스트에서 무작위로 1명을 뽑아 오늘 발표 담당자로 선정하세요.
students = ['진우', '현아', '수민', '도윤', '예린', '현수', '수진']
def randst():
    random.shuffle(students)
    one = random.choice(students)
    return one
print('오늘의 발표 담당자 : ', randst())

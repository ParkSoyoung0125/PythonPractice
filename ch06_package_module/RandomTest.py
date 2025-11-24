import random
from random import sample

# 0.0 <= 값 < 1.0
print(random.random())

# random.seed(1234)
print(random.random())

print(random.randint(1,10))

coffees = ['아메리카노','카페라떼','아이스커피','디카페인커피','바닐라라떼']

print(random.choice(coffees))

random.shuffle(coffees)
print(coffees)

# 로또 번호 생성
lottoNumber = [su for su in range(1,46)]
random.shuffle(lottoNumber)
print(lottoNumber)

lotto = lottoNumber[0:6]
secondlotto = lottoNumber[6:7]
print('당첨번호 : ', lotto)
print('2등번호 : ', secondlotto)

# 5게임 출력하기
def extractLottoNo():
    random.shuffle(lottoNumber)
    lotto = sorted(lottoNumber[0:6])
    secondlotto = sorted(lottoNumber[6:7])
    return lotto,secondlotto

for idx in range(1,6):
    lotto, secondlotto = extractLottoNo()
    print('당첨번호 : ', lotto)
    print('2등번호 : ', secondlotto)


# 다음 명단을 이용하여, 1조당 2명씩 조 배정을 해보세요.
MEMBER_SU = 2 # 조원 멤버 수

members = ['이민정', '최현미', '강유식', '김정식', '안미주', '심현철', '오지훈', '이한나']

def randomTeammate():
    random.shuffle(members)
    team = members[0:MEMBER_SU]
    return team

for i in range(0, len(members), MEMBER_SU):
    teams = randomTeammate()
    print(teams)

n = 3
sampling = random.sample(members,n)
print(sampling)
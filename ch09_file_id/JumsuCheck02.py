from http.cookiejar import uppercase_escaped_char

filename = 'jumsu.txt'
myencoding = 'utf-8'
jumsufile = open(filename, mode='wt', encoding=myencoding)
jumsulist = ['제시카,60.0,70.0,80.0,F','홍길동,50.0,70.0,100.0,M','유재석,60.0,70.0,80.0,M','티파니,40.0,80.0,50.0,F']
jumsufile.write('\n'.join(jumsulist)) # '\n'.join(jumsulist) → 리스트의 문자열들을 줄바꿈 문자로 이어붙이는 것.
jumsufile.close()

#모든 학생들의 시험 점수의 총점/평균/성별을 구한 다음, 파일 result.txt 파일에 기록해 보세요.
#성별은 'M'이면 '남자', 'F'이면 '여자'입니다.
#평균은 소수점 2째 자리까지 표시하도록 합니다.

#이름별 총점을 사전으로 만들어 보세요.
#사전 예시) '제시카':210, '홍길동':220, '유재석':210, '티파니':170

source = open(file=filename, mode='rt', encoding=myencoding) # 읽어올 파일

data = [item.strip() for item in source.readlines()]
print(data)

source.close()

class Student:
    def __init__(self, name, kor, eng, math, gender):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math
        self.gender = gender

    def total(self):
        total = self.kor + self.eng + self.math
        return total

    def avg(self):
        avg = self.total() / 3.0
        return avg

    def getname(self):
        return self.name

    def getgender(self):
        if self.gender == 'M':
            _gender = '남자'
        else:
            _gender = '여자'
        return _gender

students = []
for i in data:
    name, kor, eng, math, gender = i.split(',')
    s = Student(str(name), float(kor), float(eng), float(math), gender.upper())
    students.append(s)
# print(i for i in students)

destination = open(file='result.txt', mode='wt', encoding=myencoding)  # 신규 생성할 파일
for idx in students:
    student = f'{idx.getname()}/{idx.getgender()}/{idx.total()}/{idx.avg():.2f}'
    destination.write(student+'\n')
    print(student)
destination.close()
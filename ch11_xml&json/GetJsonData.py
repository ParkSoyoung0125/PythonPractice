import json

filename = 'jumsu.json'

myfile = open(file=filename, mode='rt',encoding='utf-8')
mystring = myfile.read()
print(type(mystring))
myfile.close()

print('loads 함수는 문자열을 읽어서 dict를 원소로 담고있는 list를 반환해줌.')
jsonData = json.loads(mystring)
print(type(mystring))
print(jsonData)

# 학생들의 정보를 tuple 형식으로 저장할 list 자료형
studentList = list()

for item in jsonData:
    name = item['name']
    kor = float(item['kor'])
    eng = float(item['eng'])
    math = float(item['math'])
    total = kor + eng + math

    _gender = item['gender'].upper()
    if _gender == 'M':
        gender = '남자'
    else:
        gender = '여자'

    if 'hello' in item.keys():
        hello = item['hello']
        mytuple = (name, kor, eng, math, total, gender, hello)
    else:
        mytuple = (name, kor, eng, math, total, gender)

    studentList.append(mytuple)
#end for
print(studentList)
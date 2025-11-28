import json

from ch10_regex.RegExam03 import mystring02

filename = 'HumanData01.json'

with open(filename, 'rt', encoding='utf-8') as myfile:
    mystring = myfile.read()
    jsondata = json.loads(mystring)
#end with

print(f'원본 Json 타입 : {type(jsondata)}')
print(f'요소 갯수 : {type(jsondata)}')
print()

print(jsondata)

for key in jsondata:
    name = jsondata[key]['name']
    age = jsondata[key]['age']

    # 집 주소 정보
    address = jsondata[key]['location']['address']
    street = jsondata[key]['location']['address']['street']
    city = jsondata[key]['location']['address']['city']
    gu = jsondata[key]['location']['address']['gu']

    # 연락처 정보
    contact = jsondata[key]['contact'] # 결과값은 사전 타입
    mobile = contact['mobile']
    email = contact['email']

    # 직업정보
    job_title = jsondata[key]['job']['title']
    company_name = jsondata[key]['job']['company']
    company_location = jsondata[key]['job']['company']['location']

    #skill 정보
    skills = jsondata[key]['skills']
    myskill = '%'.join(skills)

    print(f'{name},{age},{street} {city} {gu}, {mobile} / {email}/{job_title},{company_name},{company_location}/{myskill}')


import json

filename = 'humans.json'

myfile = open(filename, mode='rt', encoding='utf-8')
mystring = myfile.read()
print(mystring)
myfile.close()

jsonData = json.loads(mystring)
print(jsonData)

humanList = []
for item in jsonData:
    name = item['name']
    hobby = item['hobby']
    address = item['address']
    blood = item['blood'] + '형'
    ssn = item['ssn']
    if ssn[7] in ['1','3']:
        gender = '남자'
    else:
        gender = '여자'

    if int(ssn.index(2)) >= 50:
        birth = '1900년대생'
    else:
        birth = '2000년대생'

    mytuple = (name, hobby, address, blood, ssn,gender, birth)

    humanList.append(mytuple)

print(humanList)
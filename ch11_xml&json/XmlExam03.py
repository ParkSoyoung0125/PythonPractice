from xml.etree.ElementTree import parse

tree = parse('XmlExam03.xml')
myroot = tree.getroot() # 루트 엘리먼트 구하기

print(type(myroot))

families = myroot.findall('가족')
print(type(families))
print(f'총 가족수 : {len(families)}')

for family in families: # family : 1 가족을 의미
    print('가족 구성 정보')

    for saram in family: # saram : 1 사람을 의미
        tagName = saram.tag
        if len(saram) >= 1: #하위 엘리먼트가 있으면
            name = saram[0].text
            age = saram[1].text

            if tagName == '어머니':
                info = saram[0].attrib['정보']
                message = f'태그명 : {tagName}, 이름 : {name}, 나이 : {age}, 정보 : {info}'
            else:
                message = f'태그명 : {tagName}, 이름 : {name}, 나이 : {age}'
            print(message)
        else: #하위 엘리먼트가 없으면
            name = saram.attrib['이름']
            age = saram.attrib['나이']
            message = f'이름 : {name}, 나이 : {age}'
            print(message)
        #end if

        if len(saram) == 3: #혈액형 정보가 있는 경우
            blood = saram[2].text
            print(f'{tagName}의 혈액형 : {blood}')
            print(message)
    #end inner for

    print('-'*30)
#end outer for
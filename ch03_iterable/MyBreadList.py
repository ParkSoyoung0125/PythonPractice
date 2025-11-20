breadString = '바게트, 크로와상, 스콘, 치아바타, 나쵸, 식빵, 호밀빵, 베이글'

# split(',') : 지정된 구분자로 구분하여 list로 만들어줌, 아무것도 안넣으면 공백 기준으로 자름
breadList = breadString.split(',')
print(breadList)


# split('/') : /로 구분하여 list로 만들어줌, 위랑 결과 동일함
breadString = '바게트/ 크로와상/ 스콘/ 치아바타/ 나쵸/ 식빵/ 호밀빵/ 베이글'

breadList = breadString.split('/')

breadList.sort()

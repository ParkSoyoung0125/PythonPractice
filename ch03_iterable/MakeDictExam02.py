breads = {'바게트':100, '치아바타':200, '호밀빵':300, '베이글':400}

#1
if '스콘' not in breads:
    breads['스콘'] = 150
#2
findData = '치아바타'
breads[findData] = 250

#3
price = 300
if price not in breads.values():
    breads['브리오슈'] = price

#4
newItems = ['통밀빵','옥수수빵','크렌베리빵']
for item in newItems:
    price = breads.get(item, price)
    breads[item] = price

#5
targetList = ['옥수수빵','단팥빵']
for item in targetList:
    try:
        message = '품명 : %s, 단가 : %d' % (item, breads[item])
        print(message)
    except KeyError:
        print('%s은(는) 빵 목록에 존재하지 않습니다.' % item)
        breads[item] = price
        print(breads)
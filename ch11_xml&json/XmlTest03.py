from xml.etree.ElementTree import parse

tree = parse('Car_Info.xml')
myroot = tree.getroot()

cars = myroot.findall('car')
print(type(cars))
print(f'총 차량수 : {len(cars)}')

for car in cars:
    tagcar = car.tag

    if len(car) >= 1:
        brand = car[0].text
        model = car[1].text
        year = car[2].text
        color = car[3].text
        message = f'태그명 : {tagcar}, 브랜드 : {brand}, 모델 : {model}, 연도 : {year}, 색상 : {color}'
        print(message)
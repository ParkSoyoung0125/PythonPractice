import json

fileName02 = 'HumanData02.json'
with open(fileName02,'rt', encoding='utf-8') as myfile02:
    mystring02 = myfile02.read()
    jsondata02 = json.loads(mystring02)

recipe_dict = {'water':'물의 양','milk':'우유의 양','espresso_shot':'에스프레소 샷','chocolate':'초콜릿'}
recipe_comment = '레시피 - '

for key in jsondata02:
    # 커피 기본정보
    basic = jsondata02[key]['basic']
    name = jsondata02[key]['basic']['name']
    origin = jsondata02[key]['basic']['origin']
    roast = jsondata02[key]['basic']['roast']
    print(f'메뉴명 : {name}\n원두명 : {origin}\n로스팅강도 : {roast}')

    # 커피 레시피

    recipe = jsondata02[key]['recipe']
    recipe_comment = '' # 다음 레시피 반복 시 초기화
    for item in recipe:
        recipe_comment += f'{recipe_dict[item]} : {recipe[item]},'
    recipe_comment = recipe_comment[:-1] # 마지막에 붙는 , 없애기
    print(recipe_comment)
    # water = recipe.get('water')
    # milk = recipe.get('milk')
    # espresso_shot = recipe.get('espresso_shot')
    # chocolate = recipe.get('chocolate')
    # print(f'{water}, {milk}, {espresso_shot}, {chocolate}')

    # 커피 매장
    store = jsondata02[key]['store']
    brand = jsondata02[key]['store']['brand']
    branch = jsondata02[key]['store']['branch']
    last_brewed = jsondata02[key]['store']['last_brewed']
    status = jsondata02[key]['store']['status']
    print(f'매장명 : {brand},\n위치 : {branch},\n마지막로스팅 : {last_brewed},\n매장명 : {status}')
    print()
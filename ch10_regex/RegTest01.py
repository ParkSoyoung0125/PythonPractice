import re

def extract_by_regex(data, regExpr):
    # 정규식 regex를 사용하여 data에서 조건에 맞는 항목만 리스트로 반환함.
    pattern = re.compile(regExpr)
    result=[]

    for bean in data:
        if pattern.match(bean):
            result.append(bean)
    #end for

    return result
# end def

print('\n커피 이름 2개 문자 + 숫자 3개로 구성된 항목 찾기')
coffee_list01 = ['am123', 'la456', 'mo789', 'lat12']

regEx = '[a-zZ-Z]{2}[0-9]{3}'
pattern = re.compile(regEx)
result = extract_by_regex(coffee_list01, regEx)
print(result)



print('\n"c"로 시작하고 ".coffee"로 끝나며 숫자가 최소 2개 이상 포함된 항목 찾기')
coffee_list02 = ['c1.coffee', 'c12.coffee', 'c345.coffee', 'c9.coffee']
regEx = '^c[0-9]{2,}\.coffee$'
pattern = re.compile(regEx)
result = extract_by_regex(coffee_list02, regEx)
print(result)



print('\n"c"와 "e" 사이에 "a"가 1번 이상 반복되는 항목 찾기')
coffee_list03 = ['ce', 'cae', 'caae', 'caaae']
regEx = 'ca+e'
pattern = re.compile(regEx)
result = extract_by_regex(coffee_list03, regEx)
print(result)
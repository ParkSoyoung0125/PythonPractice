
filename = 'coffee_list.txt'
myencoding = 'UTF-8'
coffeelist = ['아메리카노','카페라떼','카푸치노','바닐라라떼','카페모카']
coffees = []
coffeefile = open(filename, mode='wt',encoding=myencoding)
for idx in coffeelist:
    i = idx.split(',')
    coffeefile.write(str(i))
coffeefile.close()

coffeefile01 = open(filename, mode='rt',encoding=myencoding)

while True:
    oneline = coffeefile.readline().strip()
    if not oneline:
        break
    print(oneline)

coffeefile01.close()

coffeefile02 = open(filename, mode='rt',encoding=myencoding)
print(coffeefile.readlines())
coffeefile02.close()

coffeefile03 = open(filename, mode='rt',encoding=myencoding)
print(coffeefile.read())
coffeefile03.close()
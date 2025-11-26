coffees = ['아메리카노','카페라떼','카푸치노','바닐라라떼','모카']
filename = 'coffee_menu.txt'
file01 = open(filename, mode='wt', encoding='utf-8')

for idx in range(len(coffees)):
    filename = 'coffees' + str(idx).zfill(2) + '.txt'
    if idx % 2 == 0:
        message = '오늘 추천 커피는 %s입니다.\n%d번째 커피 %s 부드럽게 즐기세요' % (coffees[idx],idx, coffees[idx])
        print(message+'\n',file = file01)
    else:
        message = '오늘 추천 커피는 %s입니다.\n%d번째 커피 %s 풍미가 깊어요' % (coffees[idx],idx, coffees[idx])
        print(message+'\n',file = file01)
    # menulist.append(message)

file01.close()


for i in range(0,5):
    coffees = ['아메리카노', '카페라떼', '카푸치노', '바닐라라떼', '모카']
    filename1 = 'coffee' + str(i).zfill(2) + '.txt'
    file02 = open(filename1, mode='wt', encoding='utf-8')
    message = f'나는 {filename1} 파일입니다, 커피 정보를 담습니다.\n{coffees[i]} 정보를 위한 텍스트 파일입니다.'
    print(message, file=file02)
    file02.close()
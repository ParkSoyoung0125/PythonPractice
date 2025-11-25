# Has A 관계 : 가방 클래스는 도시락 객체를 포함할 수 있음.
class Bag:
    isOpened = False # 도시락 가방 열림 여부(기본값 : 닫힘)
    dosirakList = [] # 도시락을 저장할 리스트

    def open(self):
        print('# 도시락 가방을 엽니다.')
        self.isOpened = True
    #end def open

    def close(self):
        print('# 도시락 가방을 닫습니다.')
        self.isOpened = False
    #end def close

    def put(self, dosirak):
        if self.isOpened:
            print('# 가방에 도시락을 담습니다.')
            self.dosirakList.append(dosirak)
            self.showList()
        else:
            print('# 도시락 가방이 닫혀있어서 도시락을 담을 수 없습니다.')
        #end if
    # end def put

    def showList(self):
        print('# 도시락 목록 확인')
        for item in self.dosirakList:
            print('\n이름 : %s, 단가 : %d원' % (item.name, item.price))
            print('반찬 목록 : ',end='')
            for ban in item.banchan:
                print(ban, end='#')
            #end inner for
            print()
        #end outer for
    #end def showList
# end class Bag

# 도시락 클래스는 가방 클래스의 포함 대상
class Dosirak:
    # 반찬 갯수는 가변적이어서 *기호를 붙임
    # *는 파이썬에서 내부적으로 tuple로 인식함.
    def __init__(self,name, price, *banchan):
        self.name = name
        self.price = price
        self.banchan = banchan
    #end def __init__
# end class Dosirak

mybag = Bag()

dosirak01 = Dosirak('진달래도시락',7000,'계란후라이','김','마른 멸치')
mybag.open()
mybag.put(dosirak01)
mybag.close()

dosirak02 = Dosirak('매화도시락',10000,'어묵','김치','마른 멸치', '단호박 샐러드')
mybag.open()
mybag.put(dosirak02)
mybag.close()

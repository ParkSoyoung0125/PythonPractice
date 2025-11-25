class Account:
    bankname = 'KB' # 클래스 변수

    def __init__(self, name, no, deposit): # self = 자바의 this /객체 본인을 뜻함, 매개변수에 포함되지 않음
        # 인스턴스 변수(= 클래스 변수) : self 키워드를 사용하여 선언한 변수
        self.name = name
        self.no = no
        self.deposit = deposit

    def printData(self):
        print('예금주 : %s' % self.name)
        print('계좌번호 : %d' % self.no)
        print('예치금 : %d' % self.deposit)
    #end def __init__
#end class Account

print('주거래은행 : %s' % Account.bankname)
print('-'*30)
soo = Account('김철수', 1234, 1000) # 객체 생성
soo.printData()

print('-'*30)
young = Account('박영희', 5678, 2500) # 객체 생성
young.printData()
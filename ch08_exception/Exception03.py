class lessThan5Exception(Exception): # Exception을 상속받음
    #입력된 숫자가 5 미만일 때 발생시키고자 하는 사용자 정의 예외
    def __init__(self, value):
        self.message = f'{value}는 5보다 작은 수입니다. 5 이상인 수를 입력하셔야 합니다.'
        super().__init__(self.message)

    def __str__(self): # 자바의 toSting() 개념과 유사함
        return f'lessThan5Exception 클래스 : {self.message}'
#end class lessThan5Exception


su = input('5 이상의 정수를 입력해 주세요.')

try:
    su = int(su)

    if su < 5:
        raise lessThan5Exception(su)
    else:
        print(f'{su}를 입력하셨습니다. 잘하셨습니다.')
except ValueError as err:
    print('올바른 숫자 형식을 입력해주셔야 합니다.')
    print(err)

except lessThan5Exception as err:
    print('예외 발생 : %s' % err)

except Exception as err:
    print('예외 발생 : %s' % err)
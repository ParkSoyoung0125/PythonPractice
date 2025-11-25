class MinJumsuException(Exception):
    def __init__(self, name):
        self.message = f'시험을 잘 못보셨군요.\n{name}님, 과락입니다. '
        super().__init__(self.message)

    def __str__(self): # 자바의 toSting() 개념과 유사함
        return f'{self.message}'


class FailedException(Exception):
    def __init__(self, name):
        self.message = f'조금만 더 공부하시길 바랍니다.\n{name}님, 불합격입니다. '
        super().__init__(self.message)

    def __str__(self):  # 자바의 toSting() 개념과 유사함
        return f'{self.message}'


try:
    name = input('이름 입력 : ')
    kor = int(input('국어점수 입력 : '))
    eng = int(input('영어점수 입력 : '))
    math = int(input('수학점수 입력 : '))

    avg = (kor + eng + math) / 3

    if kor < 40 or eng < 40 or math < 40:
        raise MinJumsuException(name)

    elif avg < 60:
        raise FailedException(name)

    else:
        pass

except MinJumsuException as err:
    print(err)

except FailedException as err:
    print(err)

else:
    print(f'{name}님, 합격입니다.')
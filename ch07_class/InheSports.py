class Sport:
    def __init__(self, name, entry):
        self.name = name
        self.entry = entry

    def showInfo(self):
        print('종목 : ', self.name)
        print('엔트리 : ', self.entry)

class BaseBall(Sport):
    def __init__(self,name, entry,t):
        super().__init__(name, entry)
        self.t = t

    def showInfo(self):
        super().showInfo()
        print('타율 : ', self.t)

class FootBall(Sport):
    def __init__(self,name, entry, g):
        super().__init__(name, entry)
        self.g = g

    def showInfo(self):
        super().showInfo()
        print('골수 : ', self.g)




base = BaseBall('야구', 9, 0.235)
base.showInfo()
print('-' * 20)
foot = FootBall('축구', 11, 5)
foot.showInfo()
#출력 결과
print('-' * 30)
from collections import Counter

myencoding = 'UTF-8'
memberfile01 = open(file='memdata01.csv', mode='rt', encoding=myencoding)

memlist = [i.split(',')[1].strip() for i in memberfile01.readlines()]

deptcnt = Counter(memlist)
print(deptcnt)
memberfile01.close()

class Employee:
    def __init__(self, name, dept, emp, rectest, fortest, uptest):
        self.name = name
        self.dept = dept
        self.emp = emp
        self.rectest = rectest
        self.fortest = fortest
        self.uptest = uptest

    def grade(self):
        r = self.rectest/1000
        f = self.fortest/100
        u = self.uptest/100
        gr = ((r*0.8)+(f*0.1)+(u*0.1))*100
        return gr

    def getname(self):
        return self.name

memberfile02 = open(file='memdata01.csv', mode='rt', encoding=myencoding)
myemplist = []
emplist = [i.split(',') for i in memberfile02.readlines()]
for idx in emplist:
    name = idx[0]
    dept = idx[1]
    emp = idx[2]
    rectest = float(idx[3])
    fortest = float(idx[4])
    uptest = float(idx[5])
    g = Employee(name, dept, emp, rectest, fortest, uptest)
    myemployees = (g.getname(), f"{g.grade():.2f}")
    myemplist.append(myemployees)
print(myemplist)
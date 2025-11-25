# ExcepTest02.py

def checkStudent(student):
    students = ['철수', '영희', '민수', '지영']
    if student in students:
        print('수강중인 학생입니다.')
    else:
        message = f'{student}는 존재하지 않는 학생입니다.'
        raise Exception(message)

try:
    checkList = ['철수', '훈식']
    for student in checkList:
        checkStudent(student)

except Exception as err:
    print('예외 객체 정보 : %s' % err)


try:
    su1 = 10
    su2 = '20'
    result = su1 + su2
    print(result)

    mydict = {'hong': 10, 'kim': 20}
    findKey = 'choi'
    print(mydict[findKey])

except TypeError as err:
    print('타입이 맞지 않습니다.')
    print('예외 객체 정보 : %s' % err)

except KeyError as err:
    print('존재하지 않는 Key 입니다.')
    print('예외 객체 정보 : %s' % err)

else:
    print('예외가 발생하지 않았습니다.')

finally:
    print('예외처리 구문 종료')
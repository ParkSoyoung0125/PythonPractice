salary = int(input('월급 입력 : '))

if (salary < 500 and salary >= 0):
    income = salary * 13.0
else:
    income = salary * 12.0
#end if

if income >= 0 and income < 1000:
    tax = 0
elif income >= 1000 and income < 5000:
    tax = 0.1
elif income >= 5000 and income < 7000:
    tax = 0.12
elif income >= 7000 and income < 10000:
    tax = 0.15
else:
    tax = 0.20
#end if

print('급여 : %d' % salary)
print('연봉 : %8.2f' % income)
print('세금 : %5.2f' % (income*tax))

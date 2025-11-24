def sungjuk(name, kor, eng = 50, math = 60):
    total = kor + eng + math
    avg = total / 3.0
    if avg >= 70.0:
        info =  "합격"
    else:
        info = "불합격"
    return (print('%s 학생의 정보\n'
                  '국어 : %d, 영어 : %d, 수학 : %d\n'
                  '총점 : %d, 평균 : %.2f, 합격여부 %s'
                  % (name, kor, eng, math, total, avg, info)))

sungjuk('김철수', 50, 60, 70)
sungjuk('박영희', 80)

# keyword argument
sungjuk(math = 30, eng = 90, name = '심현철', kor = 100)

# 2방식의 혼합(positional 방식 + keyword 방식 혼합)
sungjuk('권유정', 80, math = 50)

# keyword방식은 positional 방식보다 앞에 놓일 수 없음
# sungjuk(math = 50, '권유정', 80)
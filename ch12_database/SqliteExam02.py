from xml.etree.ElementTree import parse
import sqlite3

# step 01 : xml 파일 열기
tree = parse('sungjuk.xml')
myroot = tree.getroot()


# step 02 : sqlite DB 열기
conn = sqlite3.connect('student.db')
mycursor = conn.cursor()


# step 03 : 테이블 삭제 후 생성
try:
    mycursor.execute('drop table sungjuk')
except sqlite3.OperationalError:
    print('테이블이 존재하지 않습니다.')
#end try


# step 04 : xml 문서 구조 보고 테이블 만들기
sql = """
create table sungjuk(
    id text,
    subject text,
    jumsu integer
)"""
mycursor.execute(sql)

# step 05 : xml 데이터를 DB에 추가하기
data_list = [] # 데이터베이스에 추가할 행 목록

for student in myroot.iter('student'):
    sid = student.find('id').text
    subject = student.find('subject').text
    jumsu = student.find('jumsu').text
    data_list.append((sid, subject,jumsu))
#end for

# print(data_list)
sql = "insert into sungjuk values(?,?,?)"
mycursor.executemany(sql, data_list)


# step 06 : 전체 목록을 보여주는 함수 작성
def getAllStudents(dbcursor):
    for onetuple in dbcursor:
        print('아이디 : ' + onetuple[0], end = '')
        print(',과목 : ' + onetuple[1], end = '')
        print(', 점수 : ' + str(onetuple[2]))
    #end for

#end def

# step 07 : 테이블 내용 출력
sql = "select * from sungjuk"
mycursor.execute(sql)
getAllStudents(mycursor)

conn.commit() # 데이터베이스 커밋
# step 08 :
mycursor.close()
conn.close()
import cx_Oracle  # 오라클 db를 쉽게 활용 가능하게 하는 driver

# connection도 데이터와 기능을 가진 접속 객체
connection = cx_Oracle.connect(user="SCOTT", password="TIGER", dsn="xe")
print('1 ---', connection)  # 1 --- <cx_Oracle.Connection to SCOTT@xe>

# 커서도 커서 객체. 객체가 가진 메소드 활용...
cursor = connection.cursor()
print('2 ---', cursor)  # 2 --- <cx_Oracle.Cursor on <cx_Oracle.Connection to SCOTT@xe>>

# select한 결과값을 ResultSet(결과 집합)이라 표현
cursor.execute("""SELECT *FROM dept""")

for deptno, dname, loc in cursor:
    print("Values:", deptno, dname, loc)

cursor.close()
connection.close()

import cx_Oracle  # 오라클 db를 쉽게 활용 가능하게 하는 driver

# connect(): id/pw/dsn 값으로 db 접속하는 기능
connection = cx_Oracle.connect(user="hr", password="hr", dsn="xe")
print('db 접속 성공')  # 문제 없음 확인하기 위한 출력

# 접속된 db에 sql 문장 실행 및 결과값 활용 가능하게 하는 기능의 객체. 커서 포인터를 받아온다고 생각하면 됨...
# 커서는 결과값(테이블)도 가지고 있다.
cursor = connection.cursor()

# execute(): query(select, 질의) 문장 실행 가능한 함수
# 가변적인 바인딩 변수를 통해 쿼리 문장 실행
cursor.execute("""
        SELECT first_name, last_name
        FROM employees
        WHERE department_id = :did AND employee_id > :eid""",
        did = 50,
        eid = 190)

for fname, lname in cursor:
    print("Values:", fname, lname)

# 자원 반환 필수 !!
cursor.close()
connection.close()

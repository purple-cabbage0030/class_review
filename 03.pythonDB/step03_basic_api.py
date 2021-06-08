import cx_Oracle  # 오라클 db를 쉽게 활용 가능하게 하는 driver

connection = cx_Oracle.connect(user="SCOTT", password="TIGER", dsn="xe")
# print("Database version:", connection.version)
# # Database version: 11.2.0.2.0

cur = connection.cursor()

# 모든 데이터를 한꺼번에 가져오는 fetchall
# 검색된 resultset 정보를 보유한 cursor로부터 모든 resultset을 반환
# rows = cur.fetchall()
# for row in rows:
#     print(row)

# Fetch Methods https://cx-oracle.readthedocs.io/en/latest/user_guide/sql_execution.html#fetching
# for row in cur.execute("""SELECT *FROM dept"""):
#     print(row, type(row))    # tuple 객체 type으로 반환
#     print(row[0])    # tuple 객체의 첫 번째 요소 데이터 출력

# cur.execute("select * from dept")
# while True:
#     row = cur.fetchone()   # 한 row씩 튜플타입으로 반환하는 함수
#     if row is None:
#         break
#     print(row)

cur.execute("select * from dept")
num_rows = 3
while True:
    rows = cur.fetchmany(num_rows)  # resultset에서 한번에 반환받고자 하는 row 수
    if not rows:
        break
    for row in rows:
        print(row)



# 자원 반환 순서 중요. cursor가 connection보다 먼저 닫혀야 함
cur.close()
connection.close()

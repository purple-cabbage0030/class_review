# oracle driver 모듈 사용 선언
import cx_Oracle



# emp01 table create
# create table emp01 as select empno, ename from emp
# 예외 처리의 필요성!! 직접 하기!!
# 개별적으로 예외처리할 수 있음. 개별 예외에 이름 부여도 가능.
'''
def emp01_create():
    con = cx_Oracle.connect(user="SCOTT", password="TIGER", dsn="xe")
    cur = con.cursor()

    try:
        cur.execute('drop table emp01')
    except :
        print('table 미존재')   # or pass

    try:
        cur.execute('create table emp01 as select empno, ename from emp')
    except:
        print('table 생성 오류 발생')
    
    finally:
        cur.close()
        con.close()
'''

# sql문장별로 발생 가능한 예외 처리를 try~except라는 예외처리 문장 하나로 처리
# Exception as e 표현으로 발생하는 예외 정확하게 판단
def emp01_create():
    con = cx_Oracle.connect(user="SCOTT", password="TIGER", dsn="xe")
    cur = con.cursor()

    try:
        cur.execute('drop table emp01')
        cur.execute('create table emp01 as select empno, ename from emp')
    except Exception as e:
        print(e)
    
    finally:
        cur.close()
        con.close()

# what if? id, pw가 부정확한 경우에는 어떻게 해야 할까?

# emp01 query - all select / one select
# select문장: 필요로 하는 데이터가 있을 경우 parameter, 없는 경우 select *
def emp01_query():
    con = cx_Oracle.connect(user="SCOTT", password="TIGER", dsn="xe")
    cur = con.cursor()

    cur.execute("select * from emp01")

    # fetchall(): cursor로부터 모든 검색결과를 반환하는 함수
    # rows는 resultset 보유한 상태
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    con.close()

# ? empno로 해당 사원의 이름을 검색
def emp01_query_one(sel_empno):
    con = cx_Oracle.connect(user="SCOTT", password="TIGER", dsn="xe")
    cur = con.cursor()

    # 검색된 결과가 row 하나
    cur.execute("select ename from emp where empno=:sel_empno", sel_empno=sel_empno)

    # 결과가 하나의 row.
    row = cur.fetchone()
    print(row)

    cur.close()
    con.close()

# emp01 insert
# inset 시 커밋 필수
# insert into emp01 values(?, ?) --> parameter 필요
# 가변적인 데이터 적용을 위한 바인딩 변수 사용
def emp01_insert(new_empno, new_ename):
    con = cx_Oracle.connect(user="SCOTT", password="TIGER", dsn="xe")
    cur = con.cursor()

    # 문자열 표현에서의 따옴표 주의!! 똑같은 따옴표 쓰면 문자열이 잘리는 꼴

    # emp01_insert(22, '유재석')
    # step01 - 실행 시 문법 오류
    # cur.execute("insert into emp01 values(:new_empno, ':new_ename')", new_empno, new_ename)

    # step02 - 매뉴얼처럼 값을 바인딩 변수에 직접 대입
    # cur.execute("insert into emp01 values(:new_empno, ':new_ename')", new_empno=22, new_ename='유재석')

    # step03 - 함수의 파라미터로 유입되는 값 바인딩 변수에 대입. 대입연산자 오른쪽은 로컬 변수 즉 파라미터, 왼쪽은 바인딩 변수
    cur.execute("insert into emp01 values(:new_empno, :new_ename)", new_empno=new_empno, new_ename=new_ename)
    con.commit()

    cur.close()
    con.close()


# emp01 update
# update emp01 set ename=? where empno=?
# 함수 구현 시 parameter로 필요한 데이터는?
def emp01_update(empno, new_ename):
    con = cx_Oracle.connect(user="SCOTT", password="TIGER", dsn="xe")
    cur = con.cursor()

    cur.execute("update emp01 set ename=:new_ename where empno=:empno", empno=empno, new_ename=new_ename)
    con.commit()

    cur.close()
    con.close()

# emp01 delete
# delete from emp01 where empno=?
# 필요한 parameter는 empno.
def emp01_delete(del_empno):
    con = cx_Oracle.connect(user="SCOTT", password="TIGER", dsn="xe")
    cur = con.cursor()

    cur.execute("delete from emp01 where empno=:del_empno", del_empno=del_empno)
    con.commit()

    cur.close()
    con.close()   

# 참고: 현업에서 DDL 문장은 가급적 프로그램 코드에서 하지 않고 sql문장으로 작업 권장
# table 구조 변경은 가급적 최소화
# 개발되어 있는 함수를 필요에 의해서 직접 코드로 호출할 것
# python에서 실행 순서에 대한 제어 또는 python 파일을 독립적으로 실행할 때 필요한 코드
if __name__ == '__main__':
    # 호출 순서: table 생성 -> 검색 -> 저장 -> 검색 -> 수정 -> 검색 -> 삭제 -> 검색 (단위테스트 하는 프로세스)
    emp01_create()
    # emp01_insert(1, 2)   파라미터에 아무 값이나 들어가도 됨...
    # emp01_insert(22, '유재석')
    # emp01_update(7369, '스미스')
    # emp01_delete(22)
    # emp01_query_one(7934)
    # pass
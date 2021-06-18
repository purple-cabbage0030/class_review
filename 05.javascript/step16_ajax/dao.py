# emp01 table의 crud 로직을 전담하는 클래스
import cx_Oracle

class EmpDAO:
    # 사번으로 직원명, 급여를 검색해서 반환
    def empone(self, empno):
        try:
            conn = cx_Oracle.connect(user="SCOTT", password="TIGER", dsn="xe")
            cur = conn.cursor()
            try:
                cur.execute("select * from emp01 where empno=:empno", empno=empno)
                row = cur.fetchone()  # set타입으로 반환됨, 따라서 고유한 index로 각 요소 활용 가능 -> json 포맷으로 가공
                # print(row)
                # print(row[0])
                data = '{"ename":"' + row[1] + '", "sal":' + str(row[2]) + '}'
            except Exception as e:
                print(e)
        finally:
            cur.close()
            conn.close()

        return data

# if __name__ == '__main__':
#     dao = EmpDAO()
#     print(dao.empone(7369))

'''
dao.py의 모든 코드들은 app.py에서 호출해서 사용
단 구현 시에 제대로 구현하는지 구현 로직별로 확인하는 단위 테스트

방법: 파일단위(모듈)별로 실행 가능하게 if __name__ == '__main__':라는 코드로 py파일 독립적으로 실행 가능하게 해주는 독립실행 코드

'''
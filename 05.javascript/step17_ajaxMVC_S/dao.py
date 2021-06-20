import cx_Oracle
from dto import EmpDTO 
import json
import collections
# collections = 데이터를 관리하는 자료구조 집합을 의미. 스택, 큐, ...
# 데이터를 어떤 구조로 관리할 것인가가 자료구조. 자료구조를 지원하는 library 이름이 collectoins

class EmpDAO:
    def empdelete(self, dto):
        conn = cx_Oracle.connect(user="SCOTT", password="TIGER", dsn="xe")
        cur = conn.cursor()

        cur.execute("delete from emp01 where empno=:empno", empno=dto.getEmpno())
        conn.commit()

        cur.close()
        conn.close()


    def empupdate(self, dto):
        conn = cx_Oracle.connect(user="SCOTT", password="TIGER", dsn="xe")
        cur = conn.cursor()

        cur.execute("update emp01 set ename=:ename, sal=:sal where empno=:empno", \
                    ename=dto.getEname(), empno=dto.getEmpno(), sal=dto.getSal())
        conn.commit()

        cur.close()

    # 한명의 직원 등록
    def empinsert(self, dto):    # EmpDTO 객체를 통으로 매개변수 값으로 받을 예정
        # insert into emp01 values (1234, 'test', 200);
        conn = cx_Oracle.connect(user="SCOTT", password="TIGER", dsn="xe")
        cur = conn.cursor()

        try:
            cur.execute("insert into emp01 values (:empno, :ename, :sal)", \
                empno=dto.getEmpno(), ename=dto.getEname(), sal=dto.getSal()) 
            print("------------")
            conn.commit()
        except Exception as e:
            print(e) 

        finally:
            cur.close() 
            conn.close()


    # 한명의 직원 정보 반환
    def empone(self, empno):  

        data = ''
        try:
            conn = cx_Oracle.connect(user="SCOTT", password="TIGER", dsn="xe")
            cur = conn.cursor()

            try:
                cur.execute("select * from emp01 where empno=:v", v=empno) 
                row = cur.fetchone() 
                data = '{"ename":"' + row[1] + '", "sal":' + str(row[2]) +'}'

            except Exception as e:
                print(e) 

        except Exception as e:
            print(e) 

        finally:
            cur.close() 
            conn.close()

        return data

# 모든 직원 검색해서 반환 JSON 포맷으로 가공해서 반환하는 식으로
# 동기 발식으로 요청 <-> 응답
# 모든 직원 정보 응답 시 구조는 보편적으로 선호하는 JSON 포맷으로
# Rest API는 url의 요청 방식도 처리 로직 + url 이름도 처리 로직
# Rest API - url 정보가 요청처리 리소스 + JSON 포맷으로 응답(비동기로 응답할 수밖에 없음) - 권장하는 구조
# python에서 json 포맷 지원해주는 모듈 json 사용할 것
    def empall(self):  

        data = []
        try:
            conn = cx_Oracle.connect(user="SCOTT", password="TIGER", dsn="xe")
            cur = conn.cursor()

            try:
                cur.execute("select * from emp01") 
                rows = cur.fetchall()

                # json 포맷으로 가공: empno/ename/sal key; json 배열
                # 다양한 방법 중에 ordered dictionary 형태로 만들 것. 리스트 안에 json 포맷의 데이터
                # 저장하는 순서를 유지하는 구조의 dict 클래스
                v = []   # v 변수에 python의 dict 구조로 저장 -> data 변수로 json 포맷으로 변환
                for row in rows:
                    # print(row[0], row[1], row[2])
                    d = collections.OrderedDict()
                    d['empno'] = row[0]
                    d['ename'] = row[1]
                    d['sal'] = row[2]
                    v.append(d)  # 이미 존재하는 list의 마지막 요소로 저장

                data = json.dumps(v, ensure_ascii = False)  # json 포맷으로 자동 변환해주는 json 라이브러리의 메소드. 한글 유니코드 출력 방지 코드

            except Exception as e:
                print(e) 

        except Exception as e:
            print(e) 

        finally:
            cur.close() 
            conn.close()

        return data




if __name__ == "__main__":
    dao = EmpDAO()
    # dto = EmpDTO(2, 't', 20)
    # dao.empinsert(dto)
    dao.empall()


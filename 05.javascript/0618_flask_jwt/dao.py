import cx_Oracle
from dto import EmpDTO 
import json
import collections

class EmpDAO:

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




# if __name__ == "__main__":
#     dao = EmpDAO()
#     # dto = EmpDTO(2, 't', 20)
#     # dao.empinsert(dto)
#     dao.empall()


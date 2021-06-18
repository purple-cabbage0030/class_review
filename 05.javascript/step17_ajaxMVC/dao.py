import cx_Oracle
from dto import EmpDTO

class EmpDAO:
    def empdelete(self,):
        pass


    def empupdate(self, empno):
        try:
            conn = cx_Oracle.connect(user="SCOTT", password="TIGER", dsn="xe") 

            try:
                cur = conn.cursor()
                cur.execute("update emp01 set sal=:sal where empno=:empno)",\
                     empno=empno, sal=dto.getSal())
                conn.commit()
            except Exception as e:
                print(e)

        except Exception as e:
            print(e)
        finally:
            cur.close()
            conn.close()


    # 한 명의 직원 등록
    def empinsert(self, dto):   # 호출 시에 EmpDTO 객체를 통으로 매개변수 값으로 받을 예정
        try:
            conn = cx_Oracle.connect(user="SCOTT", password="TIGER", dsn="xe") 

            try:
                cur = conn.cursor()
                cur.execute("insert into emp01 values(:empno, :ename, :sal)",\
                     empno=dto.getEmpno(), ename=dto.getEname(), sal=dto.getSal())
                # print("-------------")   # insert 제대로 됐는지 확인
                conn.commit()
            except Exception as e:
                print(e)

        except Exception as e:
            print(e)
        finally:
            cur.close()
            conn.close()


    # 한 명의 직원 정보 반환
    def empone(self, empno):
        try:
            conn = cx_Oracle.connect(user="SCOTT", password="TIGER", dsn="xe")
            cur = conn.cursor()
            try:
                cur.execute("select * from emp01 where empno=:empno", empno=empno)
                row = cur.fetchone()
                data = '{"ename":"' + row[1] + '", "sal":' + str(row[2]) + '}'
            except Exception as e:
                print(e)
        except Exception as e:
            print(e)
        finally:
            cur.close()
            conn.close()

        return data

# if __name__ == '__main__':
    # print(dao.empone(7369))
    # dao = EmpDAO()
    # dto = EmpDTO(2, 'test', 200)
    # dao.empinsert(dto)

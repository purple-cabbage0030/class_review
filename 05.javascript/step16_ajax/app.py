from flask import Flask, render_template, request
from dao import EmpDAO

app = Flask(__name__)

# methods 속성 생략 시 get 방식
@app.route('/', methods=['get'])
def get():
    return render_template('reqres.html')

@app.route('/getdata', methods=['get'])
def getdata():
    print("getdata() ------------")
    return '{"name":"재석", "age":40}'

@app.route('/getemp', methods=['post'])
def getemp():

    empno = request.form.get('empno')   # 어떻게 client가 전송하는 데이터를 획득할 수 있는지?
    # print(empno)

    dao = EmpDAO()    # empone() 메소드를 보유한 객체 생성
    data = dao.empone(empno)   # select 후에 json 포맷의 문자열로 가공해서 반환하는 메소드 호출

    return data

@app.route('/insert', methods=['get'])
def insert():
    pass

if __name__ == '__main__':
    app.run(debug=True, host="127.0.0.1", port="5000")

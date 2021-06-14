from flask import Flask, render_template

# client가 요청 시에 서버에 전송하는 데이터를 활용할 수 있는 api
from flask import request

app = Flask(__name__)

# 첫 요청 시 step04request.html로 렌더링
# get 방식 처리 권장
# http://127.0.0.1:5000 or http://127.0.0.1:5000/ 자동으로 슬래쉬 붙음
@app.route('/')
def index():
    return render_template('step04request.html')

# request의 form tag에 입력된 데이터를 받아서 처리하는 함수 개발
# http://127.0.0.1:5000/login --> 보안을 위해 post 방식으로 처리
@app.route('/login', methods=['post'])
def login():

    # <input type="text" id="ID" name="ID" value="test">
    # name 속성 값이 ID 인 태그의 value값을 획득하는 로직
    # print('-------', request.form.get('ID'))

    ID = request.form.get('ID')

    # client가 입력한 id/pw 데이터 획득해서 검증 로직 후에 유무효 화면(step04response.html)으로 이동
    # 로직: app04에서 html로 데이터 넘겨야 함. html에서는 전송받은 데이터값을 출력하는 기능의 코드 필요.
    # return render_template('step04response.html', idencore=ID)

    # 서버에서 데이터를 새로 구성해서 출력담당 코드로 데이터 전달도 가능
    # 데이터가 다수일 때 데이터 구분을 위해서는 key와 value로 맵핑된 구조인 json 포맷 사용
    info = {"name":"재석", "age":30}

    # idencore와 userinfo는 데이터 구분용 key, 오른쪽에 있는 애들은 value
    # info 변수 선언 안 하고 json포맷 통째로 대입해도 됨.
    return render_template('step04response.html', idencore=ID, userinfo=info)

# 



if __name__ == '__main__':
    app.run(debug=True)

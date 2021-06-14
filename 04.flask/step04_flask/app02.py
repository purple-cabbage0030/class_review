# html로 응답 지시()
from flask import Flask, render_template
# get인지 post인지 방식 구분하는 api
from flask import request


app = Flask(__name__)


# http://127.0.0.1:5000/ 로 직접 브라우저에서 요청 - get방식(디폴트)
# post & get 방식 적용 (여러 개 가능하게 하는 methods)
# post 방식 test - postman 또는 html form에서 post로 지정한 tag로 요청
@app.route('/', methods=['post', 'get'])
def index():
    print('요청 방식(method)확인', request.method)
    # html page 실행 즉 렌더링 지시
    # templates라는 구조는 flask에서 요구하는 구조, 따라서 폴더명을 경로에 지정하지 않아도 알아서 html파일 실행해줌
    return render_template('step02response.html')


if __name__ == '__main__':
    app.run(debug=True)
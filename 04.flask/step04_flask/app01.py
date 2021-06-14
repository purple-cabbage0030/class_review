from flask import Flask

# Flask 객체(instance) 생성
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

# url 설정 - http://ip.port/ 또는 슬래쉬 빠진 형식으로 구성
# @: 장식자
@app.route('/')
def index():
    return {"name":"이홍주"}

if __name__  == '__main__':
    # Flask로 실행하기 위한 필수 코드
    # debug=Ture 설정 시 서버가 실행 중이어도 소스 수정 및 자동 갱신이 가능(반대를 원하면 False)
    app.run(debug=True)
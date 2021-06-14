from flask import Flask
from flask_restx import Api, Resource

app = Flask(__name__)
api = Api(app)   # swagger 문서 개발 가능하게 하는 코드

@api.route('/hello')
class HelloWorld(Resource):
    # get 방식의 요청을 처리하는 get이라는 이름의 메소드
    def get(self):
        return {"hello":"world"}

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=80)

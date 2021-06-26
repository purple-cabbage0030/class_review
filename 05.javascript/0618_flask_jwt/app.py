from flask import Flask, render_template, jsonify, request
from flask_jwt_extended import *
from dao import EmpDAO


app = Flask(__name__)

app.config.update(
    DEBUG = True,
    JWT_SECRET_KEY = "LeeHongJu"
)

jwt = JWTManager(app)

# 임시 id/pw 차후에는 DAO로 select를 해야 하는 데이터
member_id = "hello"
member_pw = "1234"

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login_proc():
    user_id = request.form.get("user_id")
    user_pw = request.form.get("user_pw")

    if user_id == member_id and user_pw == member_pw:
        return jsonify(
            result = "200",
            access_token = create_access_token(identity = user_id)
        ) and render_template("welcome.html")

    else:
        return "존재하지 않는 사용자입니다."



@app.route('/emplist', methods=["get"])
@jwt_required()
def emplist():
    cur_user = get_jwt_identity()
    print(cur_user)
    dao = EmpDAO()
    return dao.empall()

# @app.route('/emplist', methods=["get"])
# @jwt_required
# def emplist():
#     cur_user = get_jwt_identity()
#     if cur_user is None:
#         return "Member Only"
#     else:
#         return "Hi" + cur_user and EmpDAO.empall()

if __name__ == '__main__':
    app.run(debug=True, host="127.0.0.1", port="5000")


'''
참고 링크
https://m.blog.naver.com/shino1025/221954027152
header Authorizatoin + Bearer + 토큰 값
'''
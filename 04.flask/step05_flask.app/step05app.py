from flask import Flask, render_template
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('step05request.html')

@app.route('/login', methods=['post'])
def login():


    ID = request.form.get('ID')
    info = {"name":"홍주", "age":26, "job":"student"}

    return render_template('step05response.html', userid=ID, userinfo=info)


if __name__ == '__main__':
    app.run(debug=True)


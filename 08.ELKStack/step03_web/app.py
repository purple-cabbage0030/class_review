from flask import Flask, request, render_template
from dao import kb_per_loc

app = Flask(__name__)

@app.route("/", methods=["get"])
def index_view():
    return render_template("index.html")

@app.route("/dataget", methods=["get"])
def req_res():
    data = kb_per_loc()
    return str(data)
    # str_data = ""
    # for i in range(len(data)):
    #     str_data += str(data[i])
    # return str_data



if __name__ == '__main__':
    app.run(debug=True, host="127.0.0.1", port=5000)
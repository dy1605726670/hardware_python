import tihuan
from flask import Flask
from flask import render_template   # 导入模板渲染模块
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("admin.html")


@app.route('/condition/<command>', methods=["GET"])
def condition(command):
    print(command)
    tihuan.append_cmd(command)
    return render_template("succeeful.html", command=command)


@app.route('/singlechip/')
def singlechip():
    command = tihuan.read_cmd()
    return render_template("succeeful.html", command=command)


if __name__ == '__main__':
    # app.run(debug=True)
    app.run(host='0.0.0.0', port=7890, debug=True)
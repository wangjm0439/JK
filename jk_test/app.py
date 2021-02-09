from flask import Flask, render_template,url_for
from config.config import *

app = Flask(__name__)


# 启始页
@app.route('/')
def index():
    text = (title, bug_url, motto)
    return render_template("index.html", result=(text,))


# interfaceList页面
@app.route('/interfaceList')
def interfaceList():
    text = (1,)
    return render_template("interfacelist.html", result=(text,))


if __name__ == '__main__':
    app.run(debug="127.0.0.1", port=8090)

#!/usr/bin/python
# -*- coding=utf-8 -*-
import requests
from flask import Flask,render_template,request

app=Flask(__name__)
@app.route('/')
def index():
    return render_template("test3.html")

@app.route('/center/add')
def add():
    name=request.args.get('name')
    age=request.args.get('age')
    hobby=request.args.get('ch_id')
    return "姓名：%s 年龄：%s 爱好：%s" % (name, age, hobby)

@app.route('/runtest')
def runtest():
    name=request.args.get('name')
    age=request.args.get('age')
    hobby=request.args.getlist('ch_id')
    return "姓名：%s 年龄：%s 爱好：%s" % (name, age, hobby)

if __name__=="__main__":
    app.run(debug='127.0.0.1',port='8080')

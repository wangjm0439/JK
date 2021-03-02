#!/usr/bin/env python
# encoding: utf-8
import requests
import json

#单次接口请求，返回响应时间和响应结果
def single_req(url,data,method):
    if method=='post':
        res=requests.post(url,data=json.dumps(data))
    else:
        res = requests.get(url, data=json.dumps(data))
    res_time=res.elapsed.total_seconds()
    res_body=res.text
    return (res_body,res_time)

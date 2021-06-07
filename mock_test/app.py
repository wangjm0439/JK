from flask import Flask,request
import json
from Util.orderNo import *

app = Flask(__name__)


@app.route('/amount',methods=["POST","GET"])
def amount():
    if request.method=='POST':
        req_data = json.loads(request.data)
        amount=req_data["transAmt"]
        data1={
        "data": {
            "bizOrderNo": req_data["bizOrderNo"],
            "bizStatus": "SUCCESS",
            "instRespCodeAndMsg": "[E0000]-处理成功",
            "outBizNo": req_data["outBizNo"],
            "payOrderNo":orderNo(),
            "respCode": "G000",
            "respMsg": "交易成功",
            "successAmt": amount
        },
        "success": True
    }
        data2={
        "data": {
            "bizOrderNo": req_data["bizOrderNo"],
            "bizStatus": "SUCCESS",
            "instRespCodeAndMsg": "[E0001]-处理失败",
            "outBizNo": req_data["outBizNo"],
            "payOrderNo": orderNo(),
            "respCode": "G002",
            "respMsg": "交易失败",
            "successAmt": amount
        },
        "success": True
    }

        data3 = {
            "data": {
                "bizOrderNo": req_data["bizOrderNo"],
                "bizStatus": "SUCCESS",
                "instRespCodeAndMsg": "[E0002]-处理中",
                "outBizNo": req_data["outBizNo"],
                "payOrderNo": orderNo(),
                "respCode": "G001",
                "respMsg": "处理中",
                "successAmt": amount
            },
            "success": True
        }

        if amount==20:
            return data2
        if amount==30:
            return data3
        else:
            return data1



if __name__ == '__main__':
    app.run()

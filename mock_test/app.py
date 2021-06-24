from flask import Flask,request
import json
from Util.orderNo import *

app = Flask(__name__)


@app.route('/depute',methods=["POST","GET"])
def amount():
    if request.method=='POST':
        req_data = json.loads(request.data)
        amount=req_data["biz_content"]["amount"]
        loan_id=req_data["biz_content"]["out_trade_no"]
        data1={
        "data": {
            "bizOrderNo":loan_id,
            "bizStatus": "SUCCESS",
            "instRespCodeAndMsg": "[E0000]-处理成功",
            "outBizNo": loan_id,
            "payOrderNo":orderNo(),
            "respCode": "G000",
            "respMsg": "交易成功",
            "successAmt": amount
        },
        "success": True
    }
        data2={
        "data": {
            "bizOrderNo": loan_id,
            "bizStatus": "SUCCESS",
            "instRespCodeAndMsg": "[E0001]-处理失败",
            "outBizNo": loan_id,
            "payOrderNo": orderNo(),
            "respCode": "G002",
            "respMsg": "交易失败",
            "successAmt": amount
        },
        "success": True
    }

        data3 = {
            "data": {
                "bizOrderNo": loan_id,
                "bizStatus": "SUCCESS",
                "instRespCodeAndMsg": "[E0002]-处理中",
                "outBizNo": loan_id,
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

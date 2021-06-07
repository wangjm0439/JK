#!/usr/bin/python
# -*- coding=utf-8 -*-
# import requests.packages.urllib3.util.ssl_
# requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS = 'ALL'
# requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS += 'DES-CBC3-SHA'
import requests
import ssl
import http.client
import requests_pkcs12

#https 双向认证案例

def sign():
    url = "https://sandbox.99bill.com:9445/cnp/ind_auth"

    data = '''<?xml version="1.0" encoding="utf-8" standalone="yes"?>
    <MasMessage xmlns="http://www.99bill.com/mas_cnp_merchant_interface">
    <version>1.0</version><indAuthContent><merchantId>104110045112012</merchantId> 
            <terminalId>00002012</terminalId> 
                   <customerId></customerId>  
                          <externalRefNumber>20210419000000001002</externalRefNumber> 
                                  <pan>6239734964680536</pan> 
                                          <cardHolderName>王五</cardHolderName>
                                                   <idType>0</idType> 
                                                           <cardHolderId>110101199003075672</cardHolderId>       
      <phoneNO>18888888889</phoneNO></indAuthContent></MasMessage>'''

    header = {"Content-Type": "text/xml; charset=UTF-8", 'Connection': 'close',
              "Authorization": "Basic MTA0MTEwMDQ1MTEyMDEyOnZwb3MxMjM="}
    resp = requests_pkcs12.post(url, headers=header, data=(data).encode('utf-8'),
                                pkcs12_filename='10411004511201123.pfx', pkcs12_password='000000', verify=False)
    print("返回参数：", resp.text)
    print("状态码：", resp.status_code)


if __name__ == "__main__":
    sign()

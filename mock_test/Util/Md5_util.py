#!/usr/bin/env python
# encoding: utf-8

import hashlib

#加密
def encrypt(data):
    m=hashlib.md5()
    m.update(data.encode("utf-8"))
    return m.hexdigest()
#解密
def crypt(data):
    pass

if __name__=="__main__":
    print(encrypt("juiiijujd"))
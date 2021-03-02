#!/usr/bin/env python
# encoding: utf-8
import time

inputtime=time.strftime('%Y/%m/%d %H:%M:%S',time.localtime())
a=60
b=20
print(a%b,a//b,a/b)
if a%b>0:
    c=int(a//b + 1)
else:
    c=a//b
print(c)


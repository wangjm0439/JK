#!/usr/bin/env python
# encoding: utf-8
import time
import datetime

def orderNo():
    '''
    now_time=datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")[:-3] #毫秒保留3位
    #print(now_time)
    count=1
    while True:
        if count >10:
            break
        orderNo=now_time + str(count).zfill(8)
        count += 1
        #print(count)
        #print(orderNo)
        return orderNo
        '''
    #生成不重复的订单号
    time_now=time.strftime("%Y%m%d%H%M%S",time.localtime())
    orderNo =  time_now + str(int(time.time() * 100)) + str(int(time.clock() * 10000))
    return orderNo

if __name__=="__main__":
    print(orderNo())

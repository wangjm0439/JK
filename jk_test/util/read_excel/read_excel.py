#!/usr/bin/env python
# encoding: utf-8
import xlrd
from util.oper_sql.oper_sql import Oper_sql

def red_excel():
    try:
        workboot = xlrd.open_workbook(r'D:\work_space\python_space\JK\jk_test\upload\interfacedata.xlsx')
    except:
        workboot=xlrd.open_workbook(r'D:\work_space\python_space\JK\jk_test\upload\interfacedata.xls')
    table=workboot.sheet_by_index(0)
    row=table.nrows
    #print(row)
    #获取行内容添加到数据库中
    for i in range(1,row):
        data=table.row_values(i)
        add_data=Oper_sql()
        #print(data)
        add_data.insert_interfaceinfo(data[0],data[3],data[2],data[5],data[4],data[6],data[1],data[7],data[8])




if __name__=="__main__":
    red_excel()



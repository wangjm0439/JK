#!/usr/bin/env python
# encoding: utf-8
import pymysql
import time
from config.config import Config

class Oper_sql:
    def __init__(self):
        db_data=Config().my_db()
        #print(db_data)
        self.db=pymysql.connect(host=db_data[0],port=int(db_data[1]),user=db_data[2],password=db_data[3],db=db_data[4],charset=db_data[5])
        self.cursor=self.db.cursor()

    def insert_interfaceinfo(self,intername,interaddr,header,param,option,author,descp,expected,account):
        inputtime=time.strftime('%Y/%m/%d %H:%M:%S',time.localtime(time.time()))
        #print(inputtime)
        sql= "insert into interfaceinfo (intername,interaddr,header,inputtime,param,`option`,author,descp, expected,account) VALUES('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}')"\
            .format(intername,interaddr,header,inputtime,param,option,author,descp,expected,account)
        self.cursor.execute(sql)
        self.db.commit()

#列表页展示20条为一页
    def sel_interfaceinfo(self,intername,author,num=0):
        sql="select * FROM interfaceinfo where intername like '%{0}%' and author like '%{1}%'order by id Desc limit {2},20 ".format(intername,author,num)
        self.cursor.execute(sql)
        self.db.commit()
        data=self.cursor.fetchall()
        #print(data)
        return data

    #查询模块类型
    def sel_intername(self):
        sql="select distinct intername from interfaceinfo"
        self.cursor.execute(sql)
        data=self.cursor.fetchall()
        #print(data[0][0])
        self.db.commit()
        return data

    #查询开发者
    def sel_author(self):
        sql="select distinct author from interfaceinfo"
        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        #print(data[0][0])
        self.db.commit()
        return data

    #获取interfaceinfo数据总条数
    def total_num(self):
        sql="select count(*) from interfaceinfo"
        self.cursor.execute(sql)
        self.db.commit()
        data=self.cursor.fetchall()
        #print(data)
        return data

    #获取option方法分类
    def sel_option(self):
        sql=" select distinct `option` from interfaceinfo "
        self.cursor.execute(sql)
        self.db.commit()
        data=self.cursor.fetchall()
        return data


    #删除interfaceinfo
    def del_interfaceinfo(self,id):
        sql="delete from interfaceinfo where id='{0}'".format(id)
        self.cursor.execute(sql)
        self.db.commit()

    #根据id查找interfaceinfo中数据
    def sel_id_interfaceinfo(self,id):
        sql="select intername,interaddr,inputtime,param,`option`,descp, expected from interfaceinfo where id='{0}'".format(id)
        self.cursor.execute(sql)
        self.db.commit()
        data=self.cursor.fetchall()
        #print(data)
        return data

    #编辑页面显示数据， 查找interfaceinfo中的数据
    def sel_edit_interface(self,id):
        sql="select id, intername,descp,interaddr,header,param,`option`,author, expected,account from interfaceinfo where id='{0}'".format(id)
        self.cursor.execute(sql)
        self.db.commit()
        data=self.cursor.fetchall()
        #print(data[0])
        return data

    #通过编辑页面修改数据
    def update_interface(self,intername,interaddr,header,param,option,author,descp,expected,accountid,id):
        sql="update interfaceinfo set intername='{0}',interaddr='{1}',header='{2}'," \
            "param='{3}',`option`='{4}',author='{5}',descp='{6}',expected='{7}',account='{8}' where id='{9}'"\
            .format(intername,interaddr,header,param,option,author,descp,expected,accountid,id)
        self.cursor.execute(sql)
        self.db.commit()

    #查询interfacerespond
    def sel_interfacerespond(self,id,intername,result,page_num=None):
        sql="select * FROM interfacerespond where id like '%{0}%' and intername like '%{1}%'and result like '%{2}%' limit {3},20".format(id,intername,result,page_num)
        self.cursor.execute(sql)
        self.db.commit()
        data=self.cursor.fetchall()
        return data

    #写入interfacerespond
    def insert_interfacerespond(self,intername,interaddr,requestparam,respondbody,code,respondtime,descp,result):
        inputtime=time.strftime("%Y/%m/%d %H:%M:%S",time.localtime(time.time()))
        sql="insert into interfacerespond (intername,interaddr,requestparam,respondbody,`code`,respondtime,inputtime,descp,result) values('{}','{}','{}','{}','{}','{}','{}','{}','{}')"\
            .format(intername,interaddr,requestparam,respondbody,code,respondtime,inputtime,descp,result)
        self.cursor.execute(sql)
        self.db.commit()

    # 获取interfacerespond数据总条数
    def num_interfacerespond(self):
        sql="select count(*) from interfacerespond "
        self.cursor.execute(sql)
        self.db.commit()
        data=self.cursor.fetchall()
        return data

    #获取interfacerespond 中模块分类
    def sel_intername_resp(self):
        sql="select distinct intername  from interfacerespond "
        self.cursor.execute(sql)
        self.db.commit()
        data=self.cursor.fetchall()
        return data






if __name__=="__main__":
    a=Oper_sql()
    #a.insert_interfaceinfo('a','a','a','a','a','a','a','a','a')
    #a.sel_interfaceinfo()
    #a.sel_intername()
    #a.sel_author()
    #a.total_num()
    #a.del_interfaceinfo(131)
    #a.sel_interfacerespond("","","",0)
    #a.insert_interfacerespond('a','a','a','a','a','0.09','a','a')
    #a.sel_id_interfaceinfo(74)
    #a.sel_edit_interface(77)
    a.update_interface('a','a','a','a','a','a','a','a','a',133)







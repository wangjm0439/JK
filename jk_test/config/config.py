#!/usr/bin/env python
# encoding: utf-8
from configparser import ConfigParser

title="支付接口"
motto="bug的搬运工"
bug_url="http://localhost:91/zentao/bug-browse.html"

#获取数库相关配置
class Config:
    def __init__(self):
        self.cfg=ConfigParser()
        cfg_path='D:\work_space\python_space\JK\jk_test\config\db.cfg'
        self.cfg.read(cfg_path)

    # 本地数据库
    def my_db(self):
        sections=self.cfg.sections()[0]
        host=self.cfg.get(sections,'host')
        port=self.cfg.get(sections,'port')
        user=self.cfg.get(sections,'user')
        password=self.cfg.get(sections,'password')
        db=self.cfg.get(sections,'db')
        charset=self.cfg.get(sections,'charset')
        mydb=[host,port,user,password,db,charset]
        #print(mydb)
        return mydb

    # test数据库
    def test_db(self):
        sections = self.cfg.sections()[1]
        host = self.cfg.get(sections, 'host')
        port = self.cfg.get(sections, 'port')
        user = self.cfg.get(sections, 'user')
        password = self.cfg.get(sections, 'password')
        db = self.cfg.get(sections, 'db')
        charset = self.cfg.get(sections, 'charset')
        test_db = [host, port, user, password, db, charset]
        #print(test_db)
        return test_db

    # uat数据库
    def uat_db(self):
        sections = self.cfg.sections()[2]
        host = self.cfg.get(sections, 'host')
        port = self.cfg.get(sections, 'port')
        user = self.cfg.get(sections, 'user')
        password = self.cfg.get(sections, 'password')
        db = self.cfg.get(sections, 'db')
        charset = self.cfg.get(sections, 'charset')
        uat_db = [host, port, user, password, db, charset]
        #print(uat_db)
        return uat_db






if __name__=="__main__":
    a=Config()
    #a.my_db()
    #a.test_db()


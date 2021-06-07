from flask import Flask, render_template,url_for,request,send_from_directory
from config.config import *
from werkzeug.utils import secure_filename
from util.oper_sql.oper_sql import Oper_sql
from run_req.single_req import *
import os
import json

app = Flask(__name__)
my_sql=Oper_sql()

# 启始页
@app.route('/')
def index():
    text = (title, bug_url, motto)
    return render_template("index.html", result=(text,))

# interfaceList页面
@app.route('/interfaceList')
def interfaceList():
    try:
        page=int(request.args.get("page"))
        #print("页数",page)
    except:
        page=0
    #print("page",page)
    if page>0:
        data_num=(page -1) * 20  #数据条数是页数*20，如果只有一页数据及从第一条开始展示
    else:
        data_num=0
    intername=request.args.get("interface")
    author=request.args.get("author")
    if intername==None:
        intername=""
    if author==None:
        author=""
    list_data = my_sql.sel_interfaceinfo(intername,author,data_num)
    intername_list=my_sql.sel_intername()
    author_list=my_sql.sel_author()
    total_num=my_sql.total_num()[0][0]
    method=my_sql.sel_option()
    return render_template("interfacelist.html", result=(list_data,page,total_num,intername_list,author_list,method))

#addInterface新增接口
@app.route('/addInterface',methods=['POST','GET'])
def add_interface():
    if request.method=='POST':
        intername=request.form["imode"]
        interaddr=request.form["iaddr"]
        header=request.form["iheader"]
        param=request.form["iparam"]
        option=request.form["ioption"]
        author=request.form["iauthor"]
        descp=request.form["idesc"]
        expected=request.form["iresult"]
        account=request.form["iuserpwd"]
        #print(intername)
        my_sql.insert_interfaceinfo(intername,interaddr,header,param,option,author,descp,expected,account)
        return "添加成功"

#保存上传文件路径及类型判断
file_path='./upload/'
app.config['UPLOAD_FOLDER']=file_path
allow_file={'xls','xlsx'}
#文件类型判断
def allow_file_type(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allow_file

#上传文件
@app.route('/uploadfile',methods=['POST','GET'])
def upload_file():
    if request.method=='POST':
        file=request.files['myf']
        # and 判断是否有上传的文件，并且文件类型为xls或xlsx
        if file and allow_file_type(file.filename):
            filename=secure_filename(file.filename)
            file.save(os.path.join(file_path,filename))
            return "<html><p>上传成功！</p><a href='interfaceList'>返回待请求接口列表</a></html>"
        return "<html><p>上传失败</p><a href='interfaceList'>返回待请求接口列表</a></html>"

#下载模板
@app.route('/downloadfile')
def download_file():
    file_name='interfacedata.xlsx'
    return send_from_directory(r'D:\work_space\python_space\JK\jk_test\templates\file',file_name,as_attachment=True)

#删除和执行接口
@app.route('/delinterface',methods=['POST','GET'])
def delinterface():
   iid=request.args.get("iid")
   rid=request.args.get("rid")
   #print("iid:%s" % iid)
   #print("rid:%s" % rid)
   if iid !=None:
      my_sql.del_interfaceinfo(iid)
      return "<html><p>删除完成</p><a href='interfaceList'>返回待请求接口列表</a></html>"
   else:
       try:
           res_data=my_sql.sel_id_interfaceinfo(rid)
           intername=res_data[0][0]
           url=res_data[0][1]
           data=res_data[0][3]
           code=res_data[0][6]
           descp=res_data[0][5]
           method=res_data[0][4]
           res = single_req(url,data,method)
           respondbody = res[0]
           respondtime = res[1]
           # 获取响应码，根据接口具体返回进行修改
           res_code=json.loads(respondbody)["code"]
           if res_code == code:
               result="Success"
           else:
               result = "Faile"
           #将返回结果写入到数据库中,字段值转化为str格式才可写入数据库
           my_sql.insert_interfacerespond(intername,url,data,respondbody,code,respondtime,descp,result)
       except Exception as e:
           print(e)
           return "<html><p>请求异常</p><a href='interfaceList'>返回待请求接口列表</a></html>"

#编辑展示页面
@app.route('/mytest',methods=['POST','GET'])
def edit():
    if request.method=='POST':
        data=request.get_data()
        print("data",data)
        edit_id=json.loads(data)["editId"]
        print(edit_id)
        editId_data=my_sql.sel_edit_interface(str(edit_id))[0]
        #print(editId_data)
        return json.dumps({"msg": "ok", "code": 200, "data": editId_data})

#编辑修改页面
@app.route('/updateInterface',methods=['POST','GET'])
def updateinterface():
    if request.method=='POST':
        try:
            id=request.form['iid']
            intername = request.form["imode"]
            descp = request.form["idesc"]
            interaddr = request.form["iaddr"]
            header = request.form["iheader"]
            param = request.form["iparam"]
            option = request.form["ioption"]
            author = request.form["iauthor"]
            expected = request.form["iresult"]
            account = request.form["iuserpwd"]
            my_sql.update_interface(intername,interaddr,header,param,option,author,descp,expected,account,id)
            return "<html><p>添加成功</p><a href='interfaceList'>返回待请求接口列表</a></html>"
        except Exception as e:
            print(e)
            return "<html><p>添加失败</p><a href='interfaceList'>返回待请求接口列表</a></html>"


@app.route("/runtest",methods=['GET','POST'])
def all_req():
    data = request.args.getlist('ch_id')
    #print("data:", data,type(data))
    return "请求成功"



# 请求结果页面
@app.route("/interfaceRespondList")
def interfacerespindList():
    try:
        page = int(request.args.get("page"))
        #print(page)
    except:
        page=0
    if page >0:
        page_num=(page-1) * 20
    else:
        page_num =0
    id=request.args.get("myid")
    if id==None:
        id=""
    intername=request.args.get("interface")
    if intername==None:
        intername=""
    result=request.args.get("result")
    if result==None:
        result=""
    data=my_sql.sel_interfacerespond(id,intername,result,page_num)
    total_page=my_sql.num_interfacerespond()[0][0]
    intername=my_sql.sel_intername_resp()
    return render_template("interfacerespondlist.html",result=(data,total_page,page,intername))









if __name__ == '__main__':
    app.run(debug="127.0.0.1", port=8090)

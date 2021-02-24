//集成测试提交执行模块
function vailForm() {
    var obj = document.getElementsByName("iname");
    var check_val = [];
    var xhttp = new XMLHttpRequest();

    for (k in obj) {
        if (obj[k].checked) {
            check_val.push(obj[k].value);
        }
    }
    if (check_val == "") {
        alert("请选择要执行的模块");
        return false;
    }
    else {
        alert("已执行所选模块，等待执行结果");
    }
    xhttp.open("POST", "/integrate", true);
    xhttp.setRequestHeader("Content-type", "application/json");
    xhttp.send(check_val);
}

//返回列表
function fun() {
    obj = document.getElementsByName("iname");
    check_val = [];
    for (k in obj) {
        if (obj[k].checked)
            check_val.push(obj[k].value);
    }
    return check_val;
}

//编辑待请求接口给选定的接口赋值
function testbut() {
//    var aa = document.querySelectorAll('#editinter');
//    var obj = document.getElementById("editinter");
    var obj2 = document.getElementsByName("editinter2");
    var res = event['target']['value'];
    console.log(event['target']['value']);
    var modifydata = JSON.stringify({"editId": res});
    var xhttp = new XMLHttpRequest();
    xhttp.open("POST", "/mytest", true);
    xhttp.setRequestHeader("Content-type", "application/json");
    xhttp.setRequestHeader("x-requested-with", "XMLHttpRequest");
    xhttp.send(modifydata);
    //该属性每次变化时会触发
    xhttp.onreadystatechange = function () {
        //若响应完成且请求成功
        if (xhttp.readyState === 4 && xhttp.status === 200) {
            //将字符串类型转为对象
            var result = JSON.parse(xhttp.responseText);
            console.log(result);
            //输出result的数据类型
            //alert(typeof(result));
            //将对象类型转为字符串
            //var result2 = JSON.stringify(result['data']);
            var result2 = result['data'];
            //对字符串进行分割
            //var result3 = result2.toString().split(",");
            document.getElementById("editinter").value = result2[0];
            document.getElementById("emode").value = result2[1];
            document.getElementById("edesc").value = result2[2];
            document.getElementById("eaddr").value = result2[3];
            document.getElementById("eheader").value = result2[4];
            document.getElementById("eparam").value = result2[5];
            document.getElementById("eoption").value = result2[6];
            document.getElementById("eauthor").value = result2[7];
            document.getElementById("eresult").value = result2[8];
            document.getElementById("euserpwd").value = result2[9];
        }
    }
}

//使用伪类实现title属性(未使用)
function onMouseHover(ev) {
    document.styleSheets[0].insertRule('#title::before { left: ' + ev.pageX + 'px }', 0);
    document.styleSheets[0].insertRule('#title::after { left: ' + ev.pageX + 'px }', 0);
    document.getElementById('title').style.zIndex = 9999;
}

function onMouseOut() {
    document.styleSheets[0].deleteRule(0);
    document.styleSheets[0].deleteRule(0);
}

//文件转码为二进制
function fileBinary() {
    var xhttp = new XMLHttpRequest();
    var input = document.createElement("input");
    var action = "/encodefile"; //上传服务的接口地址
    var form = new FormData();
    input.type = "file";
    input.click();
    input.onchange = function () {
        var file = input.files[0];
        form.append("myf", file); //第一个参数是后台读取的请求key值
        form.append("fileName", file.name);
        form.append("type", "binary"); //实际业务的其他请求参数
        xhttp.open("POST", action);
        xhttp.send(form); //发送表单数据
        xhttp.onreadystatechange = function () {
            if (xhttp.readyState == 4 && xhttp.status == 200) {
                //var resultObj = JSON.parse(xhttp.responseText);
                var resultObj = xhttp.responseText;
                document.getElementById('shade3').classList.remove('hide');
                document.getElementById('moda3').classList.remove('hide');
                document.getElementById('encodedesc').value = resultObj;
            }
            if (xhttp.readyState == 4 && xhttp.status == 500) {
                alert('导入文件有误');
            }
        }
    }
}

//文件转码为base64
function fileBase() {
    var xhttp = new XMLHttpRequest();
    var input = document.createElement("input");
    var action = "/encodefile"; //上传服务的接口地址
    var form = new FormData();
    input.type = "file";
    input.click();
    input.onchange = function () {
        var file = input.files[0];
        form.append("myf", file); //第一个参数是后台读取的请求key值
        form.append("fileName", file.name);
        form.append("type", "base64"); //实际业务的其他请求参数
        xhttp.open("POST", action);
        xhttp.send(form); //发送表单数据
        xhttp.onreadystatechange = function () {
            if (xhttp.readyState == 4 && xhttp.status == 200) {
                //var resultObj = JSON.parse(xhttp.responseText);
                var resultObj = xhttp.responseText;
                document.getElementById('shade3').classList.remove('hide');
                document.getElementById('moda3').classList.remove('hide');
                document.getElementById('encodedesc').value = resultObj;
            }
            if (xhttp.readyState == 4 && xhttp.status == 500) {
                alert('导入文件有误');
            }
        }
    }
}

//文件转码为字符串,可作为接口参数传递
function fileStr() {
    var xhttp = new XMLHttpRequest();
    var input = document.createElement("input");
    var action = "/encodefile"; //上传服务的接口地址
    var form = new FormData();
    input.type = "file";
    input.click();
    input.onchange = function () {
        var file = input.files[0];
        form.append("myf", file); //第一个参数是后台读取的请求key值
        form.append("fileName", file.name);
        form.append("type", "filestr"); //实际业务的其他请求参数
        xhttp.open("POST", action);
        xhttp.send(form); //发送表单数据
        xhttp.onreadystatechange = function () {
            if (xhttp.readyState == 4 && xhttp.status == 200) {
                //var resultObj = JSON.parse(xhttp.responseText);
                var resultObj = xhttp.responseText;
                document.getElementById('shade3').classList.remove('hide');
                document.getElementById('moda3').classList.remove('hide');
                document.getElementById('encodedesc').value = resultObj;
            }
            if (xhttp.readyState == 4 && xhttp.status == 500) {
                alert('导入文件有误');
            }
        }
    }
}


//window.onload = function () {
//全选框
function check_all() {
    var topInp = document.getElementById("theadInp");
    var tbody = document.getElementById("tbody");
    var botInpArr = tbody.getElementsByTagName("input");

    //绑定事件
    topInp.onclick = function () {
        //优化版（被点击的input按钮的checked属性值，直接作为下面的所有的input按钮的checked属性值）
        for (var i = 0; i < botInpArr.length; i++) {
            botInpArr[i].checked = this.checked;
        }
    }
    for (var i = 0; i < botInpArr.length; i++) {
        botInpArr[i].onclick = function () {
            //定义一个标识是true还是false的变量
            //默认它为true
            var bool = true;
            //检测每一个input的checked属性值。
            for (var j = 0; j < botInpArr.length; j++) {
                if (botInpArr[j].checked == false) {
                    bool = false;
                }
            }
            topInp.checked = bool;
        }
    }
}

//拉伸表格宽度
function table_width() {
    var tTD; //用来存储当前更改宽度的Table Cell,避免快速移动鼠标的问题
    var table = document.getElementById("customers");
    for (j = 0; j < table.rows[0].cells.length; j++) {
        table.rows[0].cells[j].onmousedown = function () {
//记录单元格
            tTD = this;
            if (event.offsetX > tTD.offsetWidth - 10) {
                tTD.mouseDown = true;
                tTD.oldX = event.x;
                tTD.oldWidth = tTD.offsetWidth;
            }
//记录Table宽度
//table = tTD; while (table.tagName != ‘TABLE') table = table.parentElement;
//tTD.tableWidth = table.offsetWidth;
        };
        table.rows[0].cells[j].onmouseup = function () {
//结束宽度调整
            if (tTD == undefined) tTD = this;
            tTD.mouseDown = false;
            tTD.style.cursor = 'default';
        };
        table.rows[0].cells[j].onmousemove = function () {
//更改鼠标样式
            if (event.offsetX > this.offsetWidth - 10)
                this.style.cursor = 'col-resize';
            else
                this.style.cursor = 'default';
//取出暂存的Table Cell
            if (tTD == undefined) tTD = this;
//调整宽度
            if (tTD.mouseDown != null && tTD.mouseDown == true) {
                tTD.style.cursor = 'default';
                if (tTD.oldWidth + (event.x - tTD.oldX) > 0)
                    tTD.width = tTD.oldWidth + (event.x - tTD.oldX);
//调整列宽
                tTD.style.width = tTD.width;
                tTD.style.cursor = 'col-resize';
//调整该列中的每个Cell
                table = tTD;
                while (table.tagName != 'TABLE') table = table.parentElement;
                for (j = 0; j < table.rows.length; j++) {
                    table.rows[j].cells[tTD.cellIndex].width = tTD.width;
                }
//调整整个表
//table.width = tTD.tableWidth + (tTD.offsetWidth – tTD.oldWidth);
//table.style.width = table.width;
            }
        };
    }
}

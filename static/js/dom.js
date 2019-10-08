
//show()函数 点击 该按钮  form表单要显示出来。
function show(){
    // 操作 table
    var tb = document.getElementsByTagName('table')[1];
    // console.log(tb);
    // 设置 table 样式 display 值 block
    tb.style.display = 'block';
}

//handleData（）函数   把 表单中的数据 添加到 表格中 td
var num = 1;
function handleData() {
    //1.获取 表单中 数据
    // 获取 用户名框数据
    var user = document.getElementById('userName');
    // user.value
    var age = document.getElementById('age');
    // age.value
    var hobby = document.getElementsByName('hobby');
    var new_str = '';
    for (var i = 0; i < hobby.length; i++) {
        if (hobby[i].checked === true) {
            //
           new_str += hobby[i].value + ' ';
        }
    }
    //创建 tr
    var tr = document.createElement('tr');

    // tr.innerHTML = '<td>num</td><td></td><td></td><td></td><td></td>';
    //创建td1
    var td1 = document.createElement('td');
    //填内容
    // var txt1 = document.createTextNode(num);
    // td1.appendChild(txt1);
    td1.innerHTML = num;
    num++;
    //添加到tr
    tr.appendChild(td1);

    //创建td2
     var td2 = document.createElement('td');
    td2.innerHTML = user.value;
    //添加到tr
    tr.appendChild(td2);

    //创建td3
     var td3 = document.createElement('td');
    td3.innerHTML = age.value;
    //添加到tr
    tr.appendChild(td3);

    //创建td4
     var td4 = document.createElement('td');
    td4.innerHTML = new_str;
    //添加到tr
    tr.appendChild(td4);

    //创建td5
     var td5 = document.createElement('td');
     td5.innerHTML = '<button class="btn">删除</button>';
     tr.appendChild(td5);

     //把tr添加到table
    document.getElementById('t').appendChild(tr);

    //删除
    var btns = document.getElementsByClassName('btn');
    for (var j = 0; j < btns.length; j++) {
        btns[j].onclick = function(){
            // 删除 对应的tr
            this.parentNode.parentNode.remove();
        }
    }
}



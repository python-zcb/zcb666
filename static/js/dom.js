
//show()���� ��� �ð�ť  form��Ҫ��ʾ������
function show(){
    // ���� table
    var tb = document.getElementsByTagName('table')[1];
    // console.log(tb);
    // ���� table ��ʽ display ֵ block
    tb.style.display = 'block';
}

//handleData��������   �� ���е����� ��ӵ� ����� td
var num = 1;
function handleData() {
    //1.��ȡ ���� ����
    // ��ȡ �û���������
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
    //���� tr
    var tr = document.createElement('tr');

    // tr.innerHTML = '<td>num</td><td></td><td></td><td></td><td></td>';
    //����td1
    var td1 = document.createElement('td');
    //������
    // var txt1 = document.createTextNode(num);
    // td1.appendChild(txt1);
    td1.innerHTML = num;
    num++;
    //��ӵ�tr
    tr.appendChild(td1);

    //����td2
     var td2 = document.createElement('td');
    td2.innerHTML = user.value;
    //��ӵ�tr
    tr.appendChild(td2);

    //����td3
     var td3 = document.createElement('td');
    td3.innerHTML = age.value;
    //��ӵ�tr
    tr.appendChild(td3);

    //����td4
     var td4 = document.createElement('td');
    td4.innerHTML = new_str;
    //��ӵ�tr
    tr.appendChild(td4);

    //����td5
     var td5 = document.createElement('td');
     td5.innerHTML = '<button class="btn">ɾ��</button>';
     tr.appendChild(td5);

     //��tr��ӵ�table
    document.getElementById('t').appendChild(tr);

    //ɾ��
    var btns = document.getElementsByClassName('btn');
    for (var j = 0; j < btns.length; j++) {
        btns[j].onclick = function(){
            // ɾ�� ��Ӧ��tr
            this.parentNode.parentNode.remove();
        }
    }
}



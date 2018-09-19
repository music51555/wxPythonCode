function $(id){
    return document.getElementById(id);
}

var todo_num = 1;

// 创建localStorage.setItem(key,value)中key的方法，因为在刷新网页后，要读取出每一条存储的记录，他们的key是不同的，要保证读取出所有数据，那么就要为每一条记录生成唯一的key
function creat_todokey(){
    item_keys = [];
    if(localStorage.getItem('list')){
        var item_keys = localStorage.getItem('list').split(',');
        var todo_key = 'todo_'+ (item_keys.length+1);
    }else{
        var todo_key = 'todo_'+ todo_num;
    }
    item_keys.push(todo_key);
    localStorage.setItem('list',item_keys);
    return todo_key;
}

$('todo').onkeydown = function(){
    var bz = 'onkeydown';
    if (window.event)//如果window.event对象存在，就以此事件对象为准
        e = window.event;
        var code = e.charCode || e.keyCode;
        if (code == 13) {
            console.log($('todo').value);
            localStorage.setItem(creat_todokey(),$('todo').value);
            todo_num++;
            add_element(bz);
        }
}

function fill_value(){
    var li = document.createElement('li');
    li.innerText = $('todo').value;
}

function add_element(bz){
    var tododiv = document.createElement('div');
    tododiv.className = 'tododiv';

    $('todolist').appendChild(tododiv);

    var li = document.createElement('li');
    if(bz == 'onkeydown'){
        li.innerText = $('todo').value;
    }else{
        var todo_value = localStorage.getItem(bz);
        li.innerText = todo_value;
    }

    var listchb = document.createElement('input');
    listchb.className = 'listchb';
    listchb.type = 'checkbox';

    var todo_btn_div = document.createElement('div');
    todo_btn_div.id = 'todo_btn_div';

    var detail_btn = document.createElement('button');
    detail_btn.className = 'detail';
    detail_btn.innerText = '详细';

    var over_btn = document.createElement('button');
    over_btn.className = 'over';
    over_btn.innerText = '完成';

    var star_target = document.createElement('img');
    star_target.className = 'star_target';
    star_target.src = './images/star.png';
    this.starShow = false;  

    tododiv.appendChild(star_target);
    tododiv.appendChild(listchb);
    tododiv.appendChild(li);
    tododiv.appendChild(todo_btn_div);

    todo_btn_div.appendChild(detail_btn);
    todo_btn_div.appendChild(over_btn);

    $('todo').value = '';

    var hr = document.createElement('hr');
    tododiv.parentNode.appendChild(hr);
}

window.onload = function(){
    // 通过setItem存储的列表，通过列表的key读取出来时，是一个字符串，而不是列表，所以通过split分割，形成一个列表，循环列表中每一个值作为localStorage.getItem(key)方法中的key
    if(localStorage.getItem('list')){
        var item_keys = localStorage.getItem('list').split(',');
        for(let i = 0; i < item_keys.length; i++){
            add_element(item_keys[i]);
        }
    }

    var isShow = false;
    var detail_btns = document.getElementsByClassName('detail');
    for(var i = 0; i < detail_btns.length; i++){
        detail_btns[i].onclick = function(){
            if(isShow == false){
                this.parentNode.parentNode.children[2].style.height = '80px';
                this.innerText = '简略';
                isShow = true;
            }else{
                this.parentNode.parentNode.children[2].style.height = '20px';
                this.innerText = '详细';
                isShow = false;
            }
        }
    }

    star_list = [];
    var star_btns = document.getElementsByClassName('star_target');
    for(let i = 0; i < star_btns.length; i++){
        star_btns[i].onclick = function(){
            if(this.starShow == false){
                star_list.push(i);
                this.src = './images/star_hover.png';
                localStorage.setItem('star_list',star_list);
                this.starShow = true;
            }else{
                star_list.pop(i);
                this.src = './images/star.png';
                localStorage.setItem('star_list',star_list);
                this.starShow = false;
            }
        }
    }
   
}
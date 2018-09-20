window.onload = function(){
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

    // 在todolist中输入待办事件后，点击回车触发的事件，将输入内容添加到待办事件列表
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
                location.reload();
            }
    }

    // 在todolist输入待办事项、以及刷新网页后加载页面上的各个元素
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
        detail_btn.isShow = false;

        var del_btn = document.createElement('button');
        del_btn.className = 'delete';
        del_btn.innerText = '删除';

        var star_target = document.createElement('img');
        star_target.className = 'star_target';
        star_target.src = './images/star.png';
        star_target.starShow = false;  

        tododiv.appendChild(star_target);
        tododiv.appendChild(listchb);
        tododiv.appendChild(li);
        tododiv.appendChild(todo_btn_div);

        todo_btn_div.appendChild(detail_btn);
        todo_btn_div.appendChild(del_btn);

        $('todo').value = '';

        var hr = document.createElement('hr');
        tododiv.parentNode.appendChild(hr);
    }

    // 通过setItem存储的列表，通过列表的key读取出来时，是一个字符串，而不是列表，所以通过split分割，形成一个列表，循环列表中每一个值作为localStorage.getItem(key)方法中的key
    if(localStorage.getItem('list')){
        var item_keys = localStorage.getItem('list').split(',');
        for(let i = 0; i < item_keys.length; i++){
            add_element(item_keys[i]);
        }
    }

    // todolist每一条记录上的【详细】按钮，用于查看完整的待办事项详情，点击【详细】按钮后，增加height，按钮名称变为【隐藏】；点击【隐藏】按钮后，还原height
    var detail_btns = document.getElementsByClassName('detail');
    for(var i = 0; i < detail_btns.length; i++){
        detail_btns[i].onclick = function(){
            if(this.isShow == false){
                this.parentNode.parentNode.children[2].style.height = '80px';
                this.innerText = '简略';
                this.isShow = true;
            }else{
                this.parentNode.parentNode.children[2].style.height = '25px';
                this.innerText = '详细';
                this.isShow = false;
            }
        }
    }

    // 删除功能，点击【删除】按钮后，删除此条待办事件，并删除本条记录的星标状态，以及此条数据的列表索引
    var delete_btns = document.getElementsByClassName('delete');
    for(let i = 0; i < delete_btns.length; i++){
        delete_btns[i].onclick = function(){
            this.parentNode.parentNode.parentNode.removeChild(this.parentNode.parentNode.nextSibling);
            this.parentNode.parentNode.parentNode.removeChild(this.parentNode.parentNode);
            var list = localStorage.getItem('list').split(',');
            var star_list = localStorage.getItem('star_list').split(',');
            console.log(list);
            console.log(list.length);
            if(list.length == 1){
                list.pop();
                star_list.pop();
            }else{
                list.splice(i,1);
                star_list.splice(i,1);
            }
            console.log(list);
            localStorage.setItem('list',list);
            localStorage.setItem('star_list',star_list);
            localStorage.removeItem('todo_' + (i+1));
        }
    }

    // 刷新网页后，存储和读取待办事件列表中星标的状态
    star_list = [];
    var star_btns = document.getElementsByClassName('star_target');
    if(localStorage.getItem('star_list')){
        star_list = localStorage.getItem('star_list').split(',');
        for(let i = 0; i < star_btns.length; i++){
            if(star_list.length == 0){
                star_btns[i].src = './images/star_hover.png';
                star_list.push(i);
                localStorage.setItem('star_list',star_list);
            }else{
                for(var j = 0,k = null; j < star_list.length; j++){
                    if(i == star_list[j]){
                        star_btns[i].src = './images/star_hover.png';
                    }else{
                        star_btns[i].src = './images/star.png';
                    }
                }
            }
        }
    }

    // 点击星标后，触发的事件，将星标状态存储在localStorage中
    var star_btns = document.getElementsByClassName('star_target');
    for(let i = 0; i < star_btns.length; i++){
        star_btns[i].onclick = function(){
            if(star_list.length == 0){
                this.src = './images/star_hover.png';
                star_list.push(i);
                localStorage.setItem('star_list',star_list);
            }else{
                for(var j = 0,k = null; j < star_list.length; j++){
                    if(i == star_list[j]){
                        this.src = './images/star.png';
                        k = 'pop';
                        break;
                    }else{
                        this.src = './images/star_hover.png';
                        k = 'push';
                    }
                }
                if(k == 'pop'){
                    star_list.splice(j,1);
                }
                else{
                    star_list.push(i);
                }
                localStorage.setItem('star_list',star_list);
            }
        }
    }

    // 判断通过localStorage读取的星标记录的index，哪个与现有的li标签的索引相同，为其添加星标状态
    if(localStorage.getItem('star_list')){
        var yellow_star_list = localStorage.getItem('star_list').split(',');
        var lis = document.getElementsByTagName('li');
        for(k in yellow_star_list){
            for(i in lis){
                if(i == yellow_star_list[k]){
                    lis[i].parentNode.children[0].src = './images/star_hover.png';
                }
            }
        }
    }

    // 当鼠标浮动在待办列表中的每一条记录上时，触发的方法，将按钮显示出来
    var tododivs = document.getElementsByClassName('tododiv');
    if(tododivs[0]){
        tododivs[0].children[3].style.display = 'block';
    }
    for(var i = 0; i < tododivs.length; i++){
        tododivs[i].onmouseover = function(){
            for(var j = 0; j < tododivs.length; j++){
                tododivs[j].children[3].style.display = 'none';
            }
            // this.style.display = 'block';
            this.children[3].style.display = 'block';
        }
        tododivs[i].onmouseout = function(){
            this.children[3].style.display = 'none';
        }
    }

    var ipts = document.getElementsByClassName('listchb');
    console.log(ipts);
    var x;
    
    for(let i = 0; i < ipts.length; i++){
        ipts[i].onclick = function(){
            this.checked = true;
            var r = confirm('确认已完成待办？');
            if(r == false){
                this.checked = false;
            }else{
                $('finishlist').appendChild(this.parentNode);
                var hr = document.createElement('hr');
                $('finishlist').appendChild(hr);
                this.parentNode.children[0].src = './images/finish-hover.png';
                this.parentNode.children[0].className = 'finish-great';
                this.parentNode.removeChild(this.parentNode.children[1]);
                var list = localStorage.getItem('list').split(',');
                if( localStorage.getItem('star_list')){
                    var star_list =  localStorage.getItem('star_list').split(',');
                }
                if(list.length == 1){
                    list.pop();
                    if( localStorage.getItem('star_list')){
                        star_list.pop();
                    }
                }else{
                    list.splice(i,1);
                    if( localStorage.getItem('star_list')){
                        star_list.splice(i,1);
                    }
                }
                var finishlist = list;
                localStorage.setItem('finish_' + (i+1),localStorage.getItem('todo_' + (i+1)));
                // localStorage.setItem('finish_'+i,'finish_'+i);
                localStorage.setItem('finishlist',finishlist);
                localStorage.setItem('list',list);
                localStorage.removeItem('todo_' + (i+1));
            }
        }
    }
}
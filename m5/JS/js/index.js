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
    $('topbar-todo').onkeydown = function(){
        var bz = 'onkeydown';
        if (window.event)//如果window.event对象存在，就以此事件对象为准
            e = window.event;
            var code = e.charCode || e.keyCode;
            if (code == 13) {
                localStorage.setItem(creat_todokey(),$('topbar-todo').value);
                todo_num++;
                add_element(bz);
                location.reload();
            }
    }

    // 在todolist输入待办事项、以及刷新网页后加载页面上的各个元素
    function add_element(bz){
        var tododiv = document.createElement('div');
        tododiv.className = 'tododiv';

        var finishdiv = document.createElement('div');
        finishdiv.className = 'finishdiv';


        // 在top-bar中输入的代办事项，将其添加到待办列表中的li.innerText
        var li = document.createElement('li');
        if(bz == 'onkeydown'){
            li.innerText = $('topbar-todo').value;
        }else{
            var todo_value = localStorage.getItem(bz);
            li.innerText = todo_value;
        }

        // 创建待办列表中每一条记录所在盒子中的内容，如星标、input、按钮等
        var listchb = document.createElement('input');
        listchb.className = 'listchb';
        listchb.type = 'checkbox';

        var todo_btn_div = document.createElement('div');
        todo_btn_div.id = 'todo_btn_div';

        var finish_btn_div = document.createElement('div');
        finish_btn_div.id = 'finish_btn_div';

        var detail_btn = document.createElement('button');
        var finish_detail_btn = document.createElement('button');
        detail_btn.className = 'detail';
        detail_btn.id = 'detail_todo';
        detail_btn.innerText = '详细';
        detail_btn.isShow = false;
        finish_detail_btn.className = 'detail';
        finish_detail_btn.id = 'detail_finish';
        finish_detail_btn.innerText = '详细';
        finish_detail_btn.isShow = false;

        var del_btn = document.createElement('button');
        var finish_del_btn = document.createElement('button');
        del_btn.className = 'delete_todo';
        del_btn.id = 'delete_todo';
        del_btn.innerText = '删除';
        finish_del_btn.className = 'delete_finish';
        finish_del_btn.id = 'delete_finish';
        finish_del_btn.innerText = '删除';

        var star_target = document.createElement('img');
        star_target.className = 'star_target';
        star_target.src = './images/star.png';
        star_target.starShow = false;

        var finish_great = document.createElement('img');
        finish_great.className = 'finish_great';
        finish_great.src = './images/finish-hover.png';

        var hr = document.createElement('hr');

        var finish_li = li;
        if(bz.startsWith('todo') || bz.startsWith('on')){
            $('todolist').appendChild(tododiv);
            tododiv.appendChild(star_target);
            tododiv.appendChild(listchb);
            tododiv.appendChild(li);
            tododiv.appendChild(todo_btn_div);
            todo_btn_div.appendChild(detail_btn);
            todo_btn_div.appendChild(del_btn);
            tododiv.parentNode.appendChild(hr);
        }else if(bz.startsWith('finish')){
            $('finishlist').appendChild(finishdiv);
            finishdiv.appendChild(finish_great);
            finishdiv.appendChild(finish_li);
            finishdiv.appendChild(finish_btn_div);
            finish_btn_div.appendChild(finish_detail_btn);
            finish_btn_div.appendChild(finish_del_btn);
            finishdiv.parentNode.appendChild(hr);
        }

        $('topbar-todo').value = '';
    }

    // 在待办列表中将每一条记录，添加一个key，把这些key值存储到list列表中，将key值读取出来时，是一个字符串，而不是列表，所以通过split分割，形成一个列表，循环列表中每一个值，传入add_element方法中，将key值读取出来后，在页面刷新后，赋值给每一条记录
    if(localStorage.getItem('list')){
        var item_keys = localStorage.getItem('list').split(',');
        for(let i = 0; i < item_keys.length; i++){
            add_element(item_keys[i]);
        }
    }

    if(localStorage.getItem('finishlist')){
        var finish_keys = localStorage.getItem('finishlist').split(',');
        for(let i = 0; i < finish_keys.length; i++){
            add_element(finish_keys[i]);
        }
    }

    // todolist每一条记录上的【详细】按钮，用于查看完整的待办事项详情，点击【详细】按钮后，增加height，按钮名称变为【隐藏】；点击【隐藏】按钮后，还原height
    var detail_btns = document.getElementsByClassName('detail');
    for(var i = 0; i < detail_btns.length; i++){
        detail_btns[i].onclick = function(){
            if(this.isShow == false && this.id == 'detail_finish'){
                this.parentNode.parentNode.children[1].style.height = '80px';
                this.parentNode.parentNode.children[1].style.overflow = 'auto';
                this.innerText = '简略';
                this.isShow = true;
            }else if(this.isShow == false && this.id == 'detail_todo'){
                this.parentNode.parentNode.children[2].style.height = '80px';
                this.parentNode.parentNode.children[2].style.overflow = 'auto';
                this.innerText = '简略';
                this.isShow = true;
            }else if(this.isShow == true && this.id == 'detail_finish'){
                this.parentNode.parentNode.children[1].style.height = '25px';
                this.innerText = '详细';
                this.isShow = false;
            }else if(this.isShow == true && this.id == 'detail_todo'){
                this.parentNode.parentNode.children[2].style.height = '25px';
                this.innerText = '详细';
                this.isShow = false;
            }
        }
    }

    // 删除功能，点击【删除】按钮后，删除此条待办事件，并删除本条记录的星标状态，以及此条数据的列表索引
    var delete_btns = document.getElementsByClassName('delete_todo');
    for(let i = 0; i < delete_btns.length; i++){
        delete_btns[i].onclick = function(){
            this.parentNode.parentNode.parentNode.removeChild(this.parentNode.parentNode.nextSibling);
            this.parentNode.parentNode.parentNode.removeChild(this.parentNode.parentNode);
            var list = localStorage.getItem('list').split(',');
            if(localStorage.getItem('star_list')){
                var star_list = localStorage.getItem('star_list').split(',');
            }
            console.log(list);
            console.log(list.length);
            if(list.length == 1){
                list.pop();
                if(localStorage.getItem('star_list')){
                    star_list.pop();
                }
            }else{
                list.splice(i,1);
                if(localStorage.getItem('star_list')){
                    star_list.splice(i,1);
                }
            }
            console.log(list);
            localStorage.setItem('list',list);
            localStorage.setItem('star_list',star_list);
            localStorage.removeItem('todo_' + (i+1));
        }
    }

    //办结事项的删除按钮
    var delete_btns = document.getElementsByClassName('delete_finish');
    for(let i = 0; i < delete_btns.length; i++){
        delete_btns[i].onclick = function(){
            debugger;
            this.parentNode.parentNode.parentNode.removeChild(this.parentNode.parentNode.nextSibling);
            this.parentNode.parentNode.parentNode.removeChild(this.parentNode.parentNode);
            var finishlist = localStorage.getItem('finishlist').split(',');
            if(finishlist.length == 1){
                finishlist.pop();
            }else{
                finishlist.splice(i,1);
            }
            localStorage.setItem('finishlist',finishlist);
            localStorage.removeItem('finish_' + (i+1));
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

    // 当鼠标浮动在todo待办列表中的每一条记录上时，触发的方法，将按钮显示出来
    var tododivs = document.getElementsByClassName('tododiv');
    if(tododivs[0]){
        tododivs[0].children[3].style.display = 'block';
    }
    for(let i = 0; i < tododivs.length; i++){
        tododivs[i].onmouseover = function(){
            for(let j = 0; j < tododivs.length; j++){
                tododivs[j].children[3].style.display = 'none';
            }
            tododivs[i].children[3].style.display = 'block';
        }
        tododivs[i].onmouseout = function(){
            tododivs[i].children[3].style.display = 'none';
        }
    }

    // 当鼠标浮动在finish办结列表中的每一条记录上时，触发的方法，将按钮显示出来
    var finishdivs = document.getElementsByClassName('finishdiv');
    if(finishdivs[0]){
        console.log(finishdivs[0]);
        finishdivs[0].children[2].style.display = 'block';
    }
    for(let i = 0; i < finishdivs.length; i++){
        finishdivs[i].onmouseover = function(){
            for(let j = 0; j < finishdivs.length; j++){
                finishdivs[j].children[2].style.display = 'none';
            }
            finishdivs[i].children[2].style.display = 'block';
        }
        finishdivs[i].onmouseout = function(){
        finishdivs[i].children[2].style.display = 'none';
        }
    }

    // 点击checkbox后，将待办事件转为办结事件的方法
    var ipts = document.getElementsByClassName('listchb');
    for(let i = 0; i < ipts.length; i++){
        ipts[i].onclick = function(){
            this.checked = true;
            var r = confirm('确认已完成待办？');
            if(r == false){
                this.checked = false;
            }else{
                this.parentNode.parentNode.removeChild(this.parentNode);
                this.parentNode.className = 'finishdiv';
                this.parentNode.children[3].id = 'finish_btn_div';
                this.parentNode.children[3].children[0].className = 'detail_finish';
                this.parentNode.children[3].children[1].className = 'delete_finish';
                $('finishlist').appendChild(this.parentNode);

                var hr = document.createElement('hr');
                $('finishlist').appendChild(hr);
                this.parentNode.children[0].src = './images/finish-hover.png';
                this.parentNode.children[0].className = 'finish_great';
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

                debugger;
                if(!localStorage.getItem('finishlist')){
                    var finishlist = [];
                }else{
                    var finishlist = localStorage.getItem('finishlist').split(' ');
                }
                if(localStorage.getItem('todo_' + (i+1))){
                    var todovalue = localStorage.getItem('todo_' + (i+1));
                    if(localStorage.getItem('todo_' + (i+2))){
                        var next_todovalue = localStorage.getItem('todo_' + (i+2));
                        localStorage.setItem('todo_' + (i+1),next_todovalue)
                        localStorage.removeItem('todo_' + (i+2));
                        list.splice(i,1,'todo_' + (i+1));
                    }

                    localStorage.setItem('finish_' + (finishlist.length+1),todovalue);
                    finishlist.push('finish_' + (finishlist.length+1));
                    localStorage.setItem('finishlist',finishlist);
                    localStorage.setItem('list',list);
                    localStorage.removeItem('todo_' + (list.length+1));
                }
                if( localStorage.getItem('star_list')){
                    localStorage.setItem('star_list',star_list);
                }
                location.reload();
            }
        }
    }
}
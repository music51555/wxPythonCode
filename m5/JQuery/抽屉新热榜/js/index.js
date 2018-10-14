$(function(){
    var title = null;
    var content = null;
    var url = null;
    var j = 0;

    function loadpage(i){
        var itembanner = document.createElement('div');
        // 在刷新网页后，程序会或许当前页面的的数据条数，有多少条就会进行多少次循环，i的值 == 数据的条数
        // 在点击发布按钮后，新增数据，以j的值为准，新增第一条，第一条数据的类名为xxx0，xxx1...
        if(i != 'false'){
            itembanner.className = 'items-banner' + i;
        }else{
            itembanner.className = 'items-banner' + j;
        }
        
        // 发布帖子后，在页面创建元素
        $('.content-L').append($(itembanner));
        var newItem = document.createElement('div');
        newItem.className = 'item';
        var itemTitle = document.createElement('div');
        itemTitle.className = 'item-title';
        var itemurl = document.createElement('div');
        itemurl.className = 'item-url';
        var itemcontent = document.createElement('div');
        itemcontent.className = 'item-content';
        var itemimg = document.createElement('div');
        itemimg.className = 'item-img';
        var itempart = document.createElement('div');
        itempart.className = 'item-part';
        var commentbox = document.createElement('div');
        commentbox.className = 'comment-box';
        var tuijian = document.createElement('a');
        tuijian.className = 'tuijian';
        tuijian.innerHTML = '<span></span><b>0</b>';
        var pinglun = document.createElement('a');
        pinglun.className = 'pinglun';
        pinglun.innerHTML = '<span></span><b>0</b>';
        var sicang = document.createElement('a');
        sicang.className = 'sicang';
        sicang.innerHTML = '<span></span><b>私藏</b>';
        var lianjie = document.createElement('a');
        lianjie.className = 'lianjie';
        lianjie.innerHTML = '<span><img src = "./images/lianjie.png"></span><b>路飞特派员</b>';
        var publictime = document.createElement('a');
        publictime.className = 'public-time';

        // 发布帖子后，发布时间的更新
        var mydate = new Date();
        if(localStorage.getItem(itembanner.className+'time')){
            var refreshtime = mydate.getMinutes();
            var nowtime = localStorage.getItem(itembanner.className+'time');
            var timecha = refreshtime - nowtime;
            if (timecha < 0){
                timecha = 60 - nowtime + refreshtime;
            }
            publictime.innerHTML = '<span class="timecount">'+timecha+'分钟前</span><span class="inhot">入热榜</span>';
        }else{
            var nowtime = mydate.getMinutes();
            localStorage.setItem(itembanner.className+'time',nowtime);
            publictime.innerHTML = '<span class="timecount">小于1分钟</span><span class="inhot">入热榜</span>';
        }
        
        // 在每一个盒子下添加数据
        if(i != 'false'){
            $('.items-banner'+i).append($(newItem));
            $('.items-banner'+i).append($(itemcontent));
            $('.items-banner'+i).append($(itempart));
            $('.items-banner'+i).append($(commentbox));
            $('.items-banner'+i).append('<hr>');
        }else{
            $('.items-banner'+j).append($(newItem));
            $('.items-banner'+j).append($(itemcontent));
            $('.items-banner'+j).append($(itempart));
            $('.items-banner'+j).append($(commentbox));
            $('.items-banner'+j).append('<hr>');
        }

        // 评论盒子的HTML
        $('.comment-box').html('<div class="comment-top">\
<div class="tip1">\
最热评论(\
<span>0</span>\
)\
</div>\
<div class="tip2">\
    <span></span>\
    <a href="">去评论页面</a>\
</div>\
</div>\
<div class="comment-innerbox">\
<div class="comment-area">\
        <textarea class="comment-textarea"></textarea>\
</div>\
<a href="" class="comment-btn">评论</a>\
<span class="closehide-icon"></span>\
<a href="" class="closehide">收起</a>\
</div>\
<a href="" class="closex">X</a>');

        // 在一个盒子下添加子元素
            newItem.appendChild(itemTitle);
            
            newItem.appendChild(itemurl);
            itempart.appendChild(tuijian);
            itempart.appendChild(pinglun);
            itempart.appendChild(sicang);
            itempart.appendChild(lianjie);
            itempart.appendChild(publictime);

            // 为每一条数据复制标题、内容和URL
            if(localStorage.getItem('item-title') && i != 'false' && i != 'wenzi' && i != 'img'){
                if(i == 0){
                    itemTitle.innerText = localStorage.getItem('item-title').split(',')[i];
                    itemcontent.innerText = localStorage.getItem('item-content').split(',')[i];
                    itemurl.innerText = localStorage.getItem('item-url').split(',')[i];
                }else{
                    itemTitle.innerText = localStorage.getItem('item-title').split(',')[i-1];
                    itemcontent.innerText = localStorage.getItem('item-content').split(',')[i-1];
                    itemurl.innerText = localStorage.getItem('item-url').split(',')[i-1];
                }
            }else{
                if(i == 'false'){
                    title = itemTitle.innerText = $('.public-link-banner .public-title>input').val();
                    content = itemcontent.innerText = $('.public-link-banner .public-abs>textarea').val();
                    url = itemurl.innerText = $('.public-link-banner .add-link>input').val();
                    itemurl.innerText = $('.public-link-banner .add-link>input').val();
                }
                if(i == 'wenzi'){
                    title = itemTitle.innerText = '段子';
                    content = itemcontent.innerText = $('.public-wenzi-banner .wenzi-desc>textarea').val();
                }
                if(i == 'img'){
                    title = itemTitle.innerText = '图片';
                    content = itemcontent.innerText = $('.public-img-banner .img-desc>textarea').val();
                }
            }
            // 每一次发布后，帖子的banner+1，形成一条独立的数据
            j++;
            if(itemTitle.innerText == '图片'){
                newItem.appendChild(itemimg);
            }
        }
        if(localStorage.getItem('login-status') == 'true'){
            var finalusername = localStorage.getItem('final-username');
            $('.user-center>span').text(finalusername);
            $('.login').css('display','none');
            $('.logined').css('display','block');
        }
        if(localStorage.getItem('item-title') && $('.logined').css('display') == 'block'){
            debugger;
            titlelist = localStorage.getItem('item-title').split(',');
            console.log(titlelist);
            console.log(titlelist.length);
            if(titlelist.length > 1){
                for(let c = 1; c <= titlelist.length; c++){
                    loadpage(c);
                }
                if(localStorage.getItem('items-banner0')){
                    localStorage.setItem('items-banner1',localStorage.getItem('items-banner0'));
                    localStorage.setItem('items-banner1pinglun',localStorage.getItem('items-banner0pinglun'));
                    localStorage.removeItem('items-banner0pinglun');
                }
                localStorage.removeItem('items-banner0time');
                localStorage.removeItem('items-banner0');
                if(localStorage.getItem($('.user-center>span').text()+0)){
                    localStorage.setItem($('.user-center>span').text()+1,localStorage.getItem($('.user-center>span').text()+0));
                }
                
                // localStorage.removeItem($('.user-center>span').text()+0);
            }else{
                for(var z = 0; z < titlelist.length; z++){
                    loadpage(z);
                }
            }
            for(var i = 0; i <= titlelist.length; i++){
                if(localStorage.getItem('items-banner'+i)){
                    conment_list = localStorage.getItem('items-banner'+i).split(',');
                    console.log(conment_list);
                    $('.items-banner'+i).children('.comment-box').children('.comment-top').after('<div class="comment-content"></div>');
                    // for(var k = 0; k < conment_list.length; k++){
                    if(localStorage.getItem('items-banner'+i+'pinglun')){
                        var pinglunnames = localStorage.getItem('items-banner'+i+'pinglun').split(',');
                        for(var n = 0;n < pinglunnames.length; n++){
                            console.log(pinglunnames[n]+i);
                            if(localStorage.getItem(pinglunnames[n]+i)){
                                var user_comment_list = localStorage.getItem(pinglunnames[n]+i).split(',');
                                for(var m = 0; m < user_comment_list.length;m++){
                                    $('.items-banner'+i).children('.comment-box').children('.comment-content').append('<span class="comment-item">'+pinglunnames[n]+':'+user_comment_list[m]+'</span>');
                                }
                            }
                        }
                    }
                    // }
                    // 刷新页面后，显示当前帖子已存在的评论数
                    $('.items-banner'+i).children('.item-part').children('.pinglun').children('b').text(conment_list.length);
                    console.log($('.items-banner'+i).children('.comment-box').children('.comment-top').children('.tip1').children('span'));
                    $('.items-banner'+i).children('.comment-box').children('.comment-top').children('.tip1').children('span').text(conment_list.length);
                }
                if(localStorage.getItem('items-banner'+i+'zan')){
                    $('.items-banner'+i).children('.item-part').children('.tuijian').children('span').css('background-position','0 -20px');
                    $('.items-banner'+i).children('.item-part').children('.tuijian').children('b').text(1);
                }
            }
        }
        $('.public-btn').click(function(event){
            event.stopPropagation();
            event.preventDefault();
            if($('.logined').css('display') == 'none'){
                alert('请先登录');
            }else{
                $('.wrap').show();
            }
        });
        $('body,.content-banner,.topbar-banner,.main-content,.banner-nav').click(function(event){
            event.stopPropagation();
            $('.wrap').hide();
        });
        $('div,p,a').click(function(event){
            event.stopPropagation();
        });
        $('.public-nav-btns').children('a').click(function(event){
            event.preventDefault();
            $('.public-from').children().eq($(this).index()).show();
            $('.public-from').children().eq($(this).index()).siblings().hide();
            $(this).addClass('public-nav-active');
            $(this).siblings().removeClass('public-nav-active');
            $(this).parent().parent().siblings('.public-from').children().find('input,textarea').val('');
            $(this).parent().parent().siblings('.public-from').children().find('.public-title>input,.public-abs>textarea').attr('disabled','disabled');
            $(this).parent().parent().siblings('.public-from').children().find('.add-link-btn').css('background-position','0 -165px');
            $(this).parent().parent().siblings('.public-from').children().find('.public-go').css('background-position','0 -563px');
        });
        $('.public-module').children('a').click(function(event){
            event.preventDefault();
            if($(this).index()!=3){
                $(this).css('background-position', '0 -409px');
                $(this).siblings().css('background-position','0 -469px');
                $(this).parent().children().eq(3).css('background-position','0 -655px');
            }else{
                $(this).css('background-position', '0 -595px');
                $(this).siblings().css('background-position','0 -469px');
            }
        });
        $('.add-link>input').keyup(function(event){
            event.preventDefault();
            console.log($('.add-link>input').val());
            $('.add-link-btn').css('background-position','0 -99px');
        });
        $('.add-link-btn').click(function(event){
            event.preventDefault();
            if($('.add-link>input').val()){
                $('.public-title>input').val('路飞学城');
                $('.public-abs>textarea').val('路飞学城立志帮助有志向的年轻人通过努力学习获得体面的工作和生活!路飞学员通过学习Python，金融分析，人工智能等互联网最前沿技术，开启职业生涯新可能。');
                $('.public-title>input').removeAttr('disabled');
                $('.public-abs>textarea').removeAttr('disabled');
                $('.public-link-banner .public-go').css('background-position','0 -499px');
            }
        });
        $('.clear').click(function(event){
            event.preventDefault();
            $(this).parent().parent().find('input,textarea').val('');
            $('.add-link-btn').css('background-position','0 -165px');
            $('.public-title>input').attr('disabled','disabled');
            $('.public-abs>textarea').attr('disabled','disabled');
            $('.public-go').css('background-position','0 -563px');
        });
        $('.wenzi-desc>textarea').keyup(function(){
            $('.write-num').text(150-$(this).val().length);
            $(this).parent().parent().find('.public-go').css('background-position','0 -499px');
        });
        $('.img-desc>textarea').keyup(function(){
            $('.write-num').text(150-$(this).val().length);
            $(this).parent().parent().parent().find('.public-go').css('background-position','0 -499px');
        });
        $('.upload-btn').click(function(event){
            $('#loadfile').click();
        });
        function public(i){
            loadpage(i);
            $('.wrap').hide();
            $('.clear').click();
            if(localStorage.getItem('item-title')){
                titlelist = localStorage.getItem('item-title').split(' ');
                contentlist = localStorage.getItem('item-content').split(' ');
                urllist = localStorage.getItem('item-url').split(' ');
                titlelist.push(title);
                contentlist.push(content);
                urllist.push(url);
                localStorage.setItem('item-title',titlelist);
                localStorage.setItem('item-content',contentlist);
                localStorage.setItem('item-url',urllist);
            }else{
                localStorage.setItem('item-title',title);
                localStorage.setItem('item-content',content);
                localStorage.setItem('item-url',url);
            }
            window.location.reload();
        }
        $('.public-link-banner .public-go').click(function(event){
            event.preventDefault();
            if($('.public-link-banner .public-title>input').val()){
                var i = 'false';
                public(i);
            }
        });
        $('.public-wenzi-banner .public-go').click(function(event){
            event.preventDefault();
            if($('.public-wenzi-banner .wenzi-desc>textarea').val()){
                var i = 'wenzi';
                public(i);
            }
        });
        $('.public-img-banner .public-go').click(function(event){
            event.preventDefault();
            if($('.public-img-banner .img-desc>textarea').val()){
                var i = 'img';
                public(i);
            }
        });
        $('.item').mouseenter(function(){
            $('.item-title').css('text-decoration','underline');
        });
        $('.item').mouseleave(function(){
            $('.item-title').css('text-decoration','none');
        });
        $('.tuijian>span').click(function(event){
            event.preventDefault();
            event.stopPropagation();
            if($(this).siblings('b').text() == 0){
                $(this).css('background-position','0 - 20px');
                $(this).siblings('b').text(Number($(this).siblings('b').text()) + 1);
                console.log($(this).parent().parent().parent().get(0).className);
                localStorage.setItem($(this).parent().parent().parent().get(0).className+'zan',1);
            }else if($(this).siblings('b').text() == 1){
                $(this).css('background-position','0 - 40px');
                $(this).siblings('b').text(Number($(this).siblings('b').text()) - 1);
                localStorage.removeItem($(this).parent().parent().parent().get(0).className+'zan');
            }
        });
        $('.tuijian>span').hover(function(){
            $(this).css('background-position','0 -20px');
        },function(){
            if($(this).siblings('b').text() != 1){
                $(this).css('background-position','0 -40px');
            }
        });
        $('.pinglun>span').hover(function(){
            $(this).css('background-position','0 -60px');
        },function(){
            $(this).css('background-position','0 -100px');
        });
        $('.pinglun').click(function(event){
            if($(this).parent().siblings('.comment-box').css('display') == 'none'){
                $(this).parent().siblings('.comment-box').css('display','block');
            }else{
                $(this).parent().siblings('.comment-box').css('display','none');
            }
        });
        $('.sicang').hover(function(){
            $(this).children('span').css('background-position','0 -140px');
            $(this).children('b').css('text-decoration','underline');
        },function(){
            $(this).children('span').css('background-position','0 -160px');
            $(this).children('b').css('text-decoration','none');
        });
        var comment_value = null;
        $('.comment-textarea').keyup(function(){
            $(this).parent().siblings('.comment-btn').css('background-position','0 -33px');
            comment_value = $(this).val();
        });
        $('.comment-btn').click(function(event){
            debugger;
            event.preventDefault();
            if($(this).css('background-position') == '0px -33px'){
                if($(this).parent().siblings('.comment-content').length > 0){
                    console.log($(this).parent().siblings('comment-content'));
                    $(this).parent().siblings('.comment-content').append('<span class="comment-item"></span>');
                }else{
                    $(this).parent().before('<div class="comment-content"><span class="comment-item"></span></div>');
                }
                
                if(localStorage.getItem($(this).parent().parent().parent().attr('class'))){
                    console.log($(this).parent().parent().parent().attr('class'));
                    var commentlist = localStorage.getItem($(this).parent().parent().parent().attr('class')).split(' ');
                    commentlist.push(comment_value);
                    // for(var i = 0;i < commentlist.length;i++){
                    $(this).parent().siblings('.comment-content').children('span:last').text($('.user-center>span').text()+':'+comment_value);
                    // }
                    localStorage.setItem($(this).parent().parent().parent().attr('class'),commentlist);
                    console.log($(this).parent().parent().parent().attr('class')+$('.user-center>span').text());
                    if(localStorage.getItem($(this).parent().parent().parent().attr('class')+'pinglun')){
                        var pinglunnames = localStorage.getItem($(this).parent().parent().parent().attr('class')+'pinglun').split(',');
                        console.log(pinglunnames);
                        for(var a = 0;a < pinglunnames.length;a++){
                            if($.inArray($('.user-center>span').text(),pinglunnames) == -1){
                                pinglunnames.push($('.user-center>span').text());
                            }
                        }
                        localStorage.setItem($(this).parent().parent().parent().attr('class')+'pinglun',pinglunnames);
                    }else{
                        localStorage.setItem($(this).parent().parent().parent().attr('class')+'pinglun',$('.user-center>span').text());
                        // localStorage.setItem($('.user-center>span').text()+$(this).parent().parent().parent().attr('class').split('r')[1],comment_value);
                    }
                }else{
                    $(this).parent().siblings('.comment-content').children('span:last').text($('.user-center>span').text()+':'+comment_value);
                    localStorage.setItem($(this).parent().parent().parent().attr('class'),comment_value);
                    if(localStorage.getItem($(this).parent().parent().parent().attr('class')+'pinglun')){
                        var pinglunnames = localStorage.getItem($(this).parent().parent().parent().attr('class')+'pinglun');
                        pinglunnames.push($('.user-center>span').text());
                        localStorage.setItem($(this).parent().parent().parent().attr('class')+'pinglun',$('.user-center>span').text());
                        // localStorage.setItem($('.user-center>span').text()+$(this).parent().parent().parent().attr('class').split('r')[1],comment_value);
                    }else{
                        localStorage.setItem($(this).parent().parent().parent().attr('class')+'pinglun',$('.user-center>span').text());
                        // localStorage.setItem($('.user-center>span').text()+$(this).parent().parent().parent().attr('class').split('r')[1],comment_value);
                    }
                }
                console.log($(this).parent().parent().parent().attr('class').split('r')[1]);
                if(localStorage.getItem($('.user-center>span').text()+$(this).parent().parent().parent().attr('class').split('r')[1])){
                    var userpingluns = localStorage.getItem($('.user-center>span').text()+$(this).parent().parent().parent().attr('class').split('r')[1]).split(' ');
                    userpingluns.push(comment_value);
                    localStorage.setItem($('.user-center>span').text()+$(this).parent().parent().parent().attr('class').split('r')[1],userpingluns);
                }else{
                    localStorage.setItem($('.user-center>span').text()+$(this).parent().parent().parent().attr('class').split('r')[1],comment_value);
                }
                // $('comment-content').css('');
                $('.comment-btn').css('background-position','0px -33px');
                $(this).siblings('.comment-area').children('textarea').val('');
                // 每发布一条评论，评论数+1
                $(this).parent().siblings('.comment-top').children('.tip1').children('span').text(Number($(this).parent().siblings('.comment-top').children('.tip1').children('span').text())+1);
                $('.comment-btn').css('background-position','0px -66px');
            }
        });
        $('.closehide,.closex').click(function(event){
            event.preventDefault();
            $('.comment-textarea').val('');
            $('.comment-box').css('display','none');
        });
        $('.getyzm').click(function(event){
            event.preventDefault();
            if($('.getyzm-box>input').val() != ' ' ){
                var phonenum = Number($('.getyzm-box>input').val());
                if(!isNaN(phonenum) && $('.getyzm-box>input').val().length == 11){
                    var reg = /^130|131|132|133|134|135|136|137|138|139|186|187|188|189|177|176.{8}/g;
                    try{
                        var result = reg.exec(phonenum)[0];
                    }catch(err){
                        alert('手机号码格式不正确，请检查后重新输入');
                    }
                    if(result){
                        console.log(phonenum);
                        console.log(typeof phonenum);
                        alert('验证码是6573');
                    }
                }else{
                    alert('请输入有效的手机号码');
                }
            }else{
                alert('请先输入11位手机号码');
            }
        });
        $('.next').click(function(event){
            event.preventDefault();
            console.log($('.getyzm-box>input').val());
            console.log($('.iptyzm>input').val());
            console.log($('.iptpwd>input').val());
            if($('.getyzm-box>input').val() == ''  || $('.iptyzm>input').val() == '' || $('.iptpwd>input').val() == '' || $('.iptyzm>input').val() != '6573'){
                alert('请检查表单是否填写完整或正确');
            }else if($('.iptpwd>input').val().length < 6){
                alert('请输入6位或6位以上的密码');
            }else{
                var account = $('.getyzm-box>input').val();
                var pwd = $('.iptpwd>input').val();
                localStorage.setItem(account,pwd);
                $('.person-data').css('display','block');
                $('.login-box').css('display','none');
            }
        });
        $('.commit').click(function(event){
            event.preventDefault();
            if($('.nicheng>input').val() == ''){
                alert('起个漂亮的昵称吧');
            }else if($('.nicheng>input').val().length > 5){
                alert('昵称的长度要求5个字符或以下');
            }else{
                localStorage.setItem($('.getyzm-box>input').val()+'nicheng',$('.nicheng>input').val());
                localStorage.setItem('final-username',$('.nicheng>input').val());
                $('.person-data').css('display','none');
                $('.login-wrap').css('display','none');
                $('.user-center>span').text($('.nicheng>input').val());
                $('.login').css('display','none');
                $('.logined').css('display','block');
                alert('注册成功，即将自动登录...');
                localStorage.setItem('login-status','true');
            }
        });
        $('.login>a').click(function(event){
            event.preventDefault();
            $('.login-wrap').css('display','block');
        });
        $('.login-wrap').click(function(event){
            event.stopPropagation();
            if($('.person-data').css('display') == 'block'){

            }else{
                $('.login-wrap').css('display','none');
            }
        });
        $('.user-center').hover(function(){
            $('.more').css('display','block');
        },function(){
            $('.more').css('display','none');
        });
        $('.more').mouseenter(function(){
            $('.more').css('display','block');
        });
        $('.more').mouseleave(function(){
            $('.more').css('display','none');
        });
        $('.more').click(function(){
            var loginstatus = localStorage.getItem('login-status');
            loginstatus = 'false';
            localStorage.setItem('login-status',loginstatus);
            $('.login').css('display','block');
            $('.logined').css('display','none');
            if(localStorage.getItem('item-title')){
                debugger;
                var titlelist = localStorage.getItem('item-title').split(',');
                for(var b = 1; b <= titlelist.length;b++){
                    console.log($('.content-L>.items-banner'+b));
                    $('.content-L>.items-banner'+b).css('display','none');
                }
            }
        });
        $('.login-btn').click(function(event){
            event.preventDefault();
            if($('.login-phone>input').val() == '' || $('.login-pwd>input').val() == ''){
                alert('请完整填写用户名和密码后再试');
            }else{
                if(localStorage.getItem($('.login-phone>input').val())){
                    if(localStorage.getItem($('.login-phone>input').val()) == $('.login-pwd>input').val()){
                        alert('登录成功，'+'欢迎您回来，'+localStorage.getItem($('.login-phone>input').val()+'nicheng'));
                        localStorage.setItem('login-status','true');
                        $('.login').css('display','none');
                        $('.logined').css('display','block');
                        $('.login-box').css('display','none');
                        $('.login-wrap').css('display','none');
                        $('.user-center>span').text(localStorage.getItem($('.login-phone>input').val()+'nicheng'));
                        window.location.reload();
                    }else{
                        alert('用户名或密码错误');
                    }
                }else{
                    alert('用户名或密码错误');
                }
            }
        });
    });
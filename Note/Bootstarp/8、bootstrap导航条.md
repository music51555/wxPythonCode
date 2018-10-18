bootstarp的top导航条

`navbar`类：top导航条都继承自于该类

`navbar-default`类，设置top导航条中的字体颜色

`navbar-header`类中存储的是，当浏览器缩放至手机宽度时，展示top导航条中的缩略按钮

`sr-only`类，隐藏span标签

`icon-bar`类，表示缩略按钮下的3条横线

`navbar-left`、`navbar-right`类：表示放置在导航栏的左侧或右侧

`navbar-form`类：将表单放置在该类下，可以很好的垂直对齐，并且当浏览器视口较小时，可以呈现按钮缩略状态

`divider`类：表示分割线



所有js插件都是依赖于jquery的，所以jquery必须放在前面：

`<script type="text/javascript" src="./js/jquery.min.js"></script>`
`<script type="text/javascript" src="./bootstrap-3.3.7/js/bootstrap.min.js"></script>`

`aria-label`属性：页面中可能包含多个nav，所以使用 aria-label属性，为导航增加描述信息

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <link rel="stylesheet" href="./bootstrap-3.3.7/css/bootstrap.css">
    <style type="text/css">
        body{
            padding-top: 70px;
        }
    </style>
</head> 
<body style="height:2000px">
    <!-- 导航条都继承自于navbar类，navbar-default表示导航条中的字体颜色 -->
    <!-- 添加navbar-fixed-top类名，可以使导航栏固定在顶部 -->
    <!-- 添加navbar-fixed-bottom类名，可以使导航栏固定在底部 -->
    <!-- 添加navbar-inverse类，可以使导航条颜色变为反色 -->
    <nav class="navbar navbar-default navbar-fixed-top navbar-inverse">
        <div class="container-fluid">

            <div class="navbar-header">
                <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1" aria-expanded="false">
                    <!--sr-only表示隐藏span元素  -->
                    <span class="sr-only">Toggle navigation</span>
                    <!-- 此span标签标识浏览器缩小后，导航按钮中的三条横线 -->
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                </button>
                <!-- 将logo处设置为一张图片或网站名称 -->
                <a class="navbar-brand" href="#">
                    <img  src="./images/B.png" alt="">
                </a>
                <!-- <a class="navbar-brand" href="#">新浪网</a> -->
            </div>

            <!-- Collect the nav links, forms, and other content for toggling -->
            <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
            <ul class="nav navbar-nav">
                <li class="active">
                    <a href="#">
                        首页
                        <!--sr-only表示隐藏span元素，可用于放置图标等  -->
                        <span class="sr-only">(current)</span>
                    </a>
                </li>
                <li>
                    <a href="#">资讯</a>
                </li>
                <li>
                    <a href="#">娱乐</a>
                </li>
                <li>
                    <a href="#">体育</a>
                </li>
                <!-- 导航栏中的下拉菜单 -->
                <li class="dropdown">
                <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">更多 <span class="caret"></span></a>
                <ul class="dropdown-menu">
                    <li><a href="#">赛事</a></li>
                    <li><a href="#">文化</a></li>
                    <li><a href="#">电竞</a></li>
                </ul>
                </li>
            </ul>
            <!-- navbar-left、navbar-right表示放置在导航栏的右侧 -->
            <!-- 将表单放置在navbar-form类中，可以很好的垂直对齐，并且当浏览器视口较小时，可以呈现折叠状态 -->
            <form class="navbar-form navbar-right">
                <div class="form-group">
                <input type="text" class="form-control" placeholder="Search">
                </div>
                <!-- 为导航栏中的按钮添加navbar类名，可以呈现很好的垂直效果 -->
                <button type="submit" class="btn btn-default">Submit</button>
            </form>

            <ul class="nav navbar-nav navbar-right">
                <li class="dropdown">
                <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">个人中心 <span class="caret"></span></a>
                <ul class="dropdown-menu">
                    <li><a href="#">我的账户</a></li>
                    <li role="separator" class="divider"></li>
                    <li><a href="#">我的资料</a></li>
                    <li role="separator" class="divider"></li>
                    <li><a href="#">我的优惠券</a></li>
                    <!-- 分割线 -->
                    <li role="separator" class="divider"></li>
                    <li><a href="#">退出</a></li>
                </ul>
                </li>
            </ul>
            </div>
        </div>
    </nav>       
</body>
<!-- 所有js插件都是依赖于jquery的，所以jquery必须放在前面 -->
<script type="text/javascript" src="./js/jquery.min.js"></script>
<script type="text/javascript" src="./bootstrap-3.3.7/js/bootstrap.min.js"></script>
</html>
```


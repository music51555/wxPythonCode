jquery表单事件

**change**，选中单选、多选、下拉菜单时触发

**select,**文本框内容被选中时触发

**submit**，点击表单中的提交按钮时触发**,一定要记住，submit事件时针对于form表单的**

js中是**onsubmit**方法

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <form action="https://www.baidu.com/">
        <p>
            <input type="radio" name="sex">男
            <input type="radio" name="sex">女
        </p>
        <p>
            <label for="username">用户名</label>
            <input type="text" name="username" placeholder="请输入用户名">
        </p>
        <p>
            <input type="submit" value="提交">
        </p>
    </form>
    
    <script type="text/javascript" src="./js/jquery-3.3.1.js"></script>
    <script type="text/javascript">
        // 在选中单选、下拉菜单等控件时触发的方法
        $('[type = radio]').change(function(){
            console.log('选中了');
        });
        
        // 在选中文本框中的内容时，触发的事件
        $('[name = username]').select(function(){
            console.log('内容被选中了');
        });

        // 一定要记住，submit事件时针对于form表单的
        $('form').submit(function(e){
            e.preventDefault();
            console.log('提交了');
        });

    </script>
</body>
</html>
```


筛选选择器siblings

简单的siblings

$(this).siblings('button')，选择当前jquery对象的其他兄弟对象

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <style type="text/css">
        button{
            width: 100px;
            height: 50px;
        }
    </style>
</head>
<body>
    <button>alex1</button>
    <button>alex2</button>
    <button>alex3</button>
    <button>alex4</button>
    <script type="text/javascript" src="./js/jquery-3.3.1.js"></script>
    <script type="text/javascript">
        $('button').click(function(){
            // 设置当前jquery对象的兄弟对象的样式
            $(this).siblings('button').css('background','red');
        });
    </script>
</body>
</html>
```


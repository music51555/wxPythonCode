通过js模拟hover选择器

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
            margin: 10px;
        }
        .btn{
            background-color: green;
        }
    </style>
</head>
<body>
    <button class="btn">按钮1</button>
    <button>按钮2</button>
    <button>按钮3</button>
    <button>按钮4</button>
    <button>按钮5</button>
    <script type="text/javascript">
        var btns = document.getElementsByTagName('button');
        for(var i = 0; i < btns.length; i++){
            btns[i].onmouseover= function(){
                for(var j = 0; j < btns.length; j++){
                    btns[j].className = ' ';
                }
                this.className = 'btn';
            }
        }

        for(var j = 0; j < btns.length; j++){
                btns[j].onmouseout = function(){
                this.className = ' ';
            }
        }
    </script>
</body>
</html>
```


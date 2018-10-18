bootstrap徽章

`badge`    美 /bædʒ/  徽章，标记。给链接、按钮嵌套span，类名设置为badge导航等元素嵌套元素，可以很醒目的展示新的或未读的信息条目 

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <link rel="stylesheet" href="./bootstrap-3.3.7/css/bootstrap.css">
</head>
<body>
    <div class="container">
        <div class="row">
            <div class="col-md-4">
                <a href="#">Inbox <span class="badge">42</span></a>
                <button class="btn btn-primary" type="button">
                    Messages 
                    <span class="badge">4</span>
                </button>
            </div>
        </div>
    </div>
</body>
</html>
```


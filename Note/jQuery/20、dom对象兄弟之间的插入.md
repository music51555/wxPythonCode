dom对象兄弟之间的插入

**``当要插入的元素内容很多时，可以使用反引号圈起来**

**${变量名}如果在字符串中插入变量，可以使用此格式**

$(A)**.after**($(B))，表示在A的后面插入B

$(A)**.insertAfter**($(B)，表示把A插入到B的后面

$(A)**.before**$(B)，表示在A的前面插入B

$(A)**.insertBefore**$(B)，表示把A插入到B的前面

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
    <ul>
        <li class="li">alex</li>
    </ul>
    <script type="text/javascript" src="./js/jquery-3.3.1.js"></script>
    <script type="text/javascript">
        // ``当要插入的元素内容很多时，可以使用反引号圈起来
        // $(A).after($(B))，表示在A的后面插入B
        $('.li').after(`
            <li>wxx
                <a href='https://www.baidu.com'>百度</a>
            </li>
        `);

        // $(A).insertAfter($(B)，表示把A插入到B的后面
        $('<li>egon</li>').insertAfter($('.li'));
        
        // $(A).before$(B)，表示在A的前面插入B
        $('.li').before('<li>xiaoma</li>');
            
        // $(A).insertBefore$(B)，表示把A插入到B的前面
        $('<li>luffy</li>').insertBefore($('.li'));

        /*
        xiaoma
        luffy
        alex
        egon
        wxx 百度
        */
    </script>
</body>
</html>
```


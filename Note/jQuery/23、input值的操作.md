点击**单选按钮radio**触发事件的方法

JS：**onchange**

Jquery：**change**

设置单选按钮默认被选中



主要的思想是添加**“:selected”**，表示拥有某个属性的标签

$('select').find('option:selected')



**JS对象.selectedIndex**表示设置被选中的索引序号，将其设置为选中

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
    // 只有name的值相同，单选按钮才能起到互斥效果
    男<input type="radio" name="sex">
    女<input type="radio" name="sex">

    <select>
        <option value="alex">alex</option>
        <option value="wxx" selected>wxx</option>
        <option value="egon">egon</option>
    </select>
    <script type="text/javascript" src="./js/jquery-3.3.1.js"></script>
    <script type="text/javascript">
        // 设置jquery对象的checked属性为true，默认为选中
        $('input[type = radio]').eq(0).attr('checked',true);

        // 点击单选按钮时所触发的事件change，在函数中打印单选按钮的val值
        $('input[type = radio]').change(function(){
            alert(1);
            // 如果单选按钮被选中，则他的val()值为on，所以通过判断如果值为on的时候做哪些事
            console.log($(this).val());
            // 或通过jquery对象：属性.val()来输出属性值
            console.log($('input[type = radio]:checked').val());
        });
        
        // 获取jquery对象下selected属性的value值
        console.log($('select option:selected').val());

        // 通过get(1)得到的JS对象，以JS对象.属性 = xxx的方式设置属性值，将他的selected的值设置为true，被选中
        $('select option').get(1).selected = true;

        // 通过get(1)得到的JS对象，selectedIndex表示被选中的索引序号，将对象被选中的索引设置为0，表示选中第一个
        $('select').get(0).selectedIndex = 0;

        $('select').change(function(){
            console.log($(this).val());
            console.log($('select').find('option:selected').text());
            
            // selectedIndex是通过get(0)转换为JS对象后，获取当前选中的JS对象的索引的方法
            // get(0)表示将jquery对象转换为JS对象
            console.log($(this).get(0).selectedIndex);
            
            // index()方法表示获取当前jquery对象的索引方法
            console.log($(this).index());
        });
    </script>
</body>
</html>
```


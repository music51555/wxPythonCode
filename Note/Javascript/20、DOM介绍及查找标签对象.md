**DOM**

Document Object Model

在html结构树中，分为head和body，在head和body中包含各个标签，形成了一个DOM树

各个标签，一切皆是节点，一切皆是对象



**DOM可以做什么**

```
DOM的工作流程
1、先找到对象（元素节点）
2、设置标签的属性值
3、设置标签的样式
4、设置标签的值
5、动态的创建和删除元素
6、事件的出发响应
	6.1 先找到事件源
	6.2 事件
	6.3 事件驱动，js事件
```



**查找元素对象**

**document.documentElement**

**document.body**

**getElementById**

**getElementsByClassName**

**getElementsByTagName**

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
    <div id="box1" class="box"></div>
    <div id="box2" class="box"></div>
    <script type="text/javascript">
        // 获取整个文档对象
        console.log(document);
        
        // 获取html，console.log()是在控制台输出内容
        console.log(document.documentElement);
        
        // console.dir()可以显示一个对象所有的属性和方法，可以查看html标签对象下的属性和方法
        console.dir(document.documentElement);

        // 获取body对象
        console.log(document.body);

        // 获取节点对象的三种方式
        // 1、通过标签id获取标签对象，获取到了id=box1的标签对象
        var box1obj = document.getElementById('box1');
        console.log(box1obj);

        // 2、通过类名获取标签对象集合Element+s
        var boxsobj = document.getElementsByClassName('box');
        console.log(boxsobj);

        // 3、通过标签名获取标签对象集合
        var divtags = document.getElementsByTagName('div');
        console.log(divtags);

        // 以...Elements查找的结果显示为：HTMLCollection(2) [div#box1.box, div#box2.box, box1: div#box1.box, box2: div#box2.box]。里面存放的是结果集合，它是一个伪数组，因为在它的__proto__方法中没有数组的方法，如push，所以既然是一个集合就可以通过索引查找到指定标签
        var divs = document.getElementsByClassName('box');
        // 将查找到集合中第一个div元素标签
        console.log(divs[0]);
        console.log(divs[1]);
    </script>
</body>
</html>
```


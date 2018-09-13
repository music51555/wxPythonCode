json继承于Object

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
    <script type="text/javascript">
        // 1、以对象的方式创建json
        var person = {
            "name":'alex',
            "age":20
        }
        console.log(person);
        // 输出Object，json继承于Object
        console.log(typeof person);

        // 2、数组方式创建
        var jsonarr = [{"name":'alex',"age":20},{"name":'wxx',"age":30}];
        console.log(jsonarr);

        // 3、json的序列化和反序列化
        // 序列化通过JSON.parse，将字符串转换为json对象
        var jsonstr = '{"name":"alex","age":20}';
        var jsonobj = JSON.parse(jsonstr);

        // 输出{name: "alex", age: 20}，Object类型
        console.log(jsonobj);
        console.log(typeof jsonobj);

        // 反序列化通过JSON.stringify()，将json对象转换为字符串
        // 输出{\"name\":\"alex\",\"age\":20}，String类型
        var jsonstr = JSON.stringify(jsonstr);
        console.log(jsonstr);
        console.log(typeof jsonstr);

        // 4、遍历JSON
        // 遍历json对象
        var person = {"name":'alex',"age":20};
        // for in的方式，k表示JSON的key
        for(var k in person){
            console.log(k+' '+person[k]);
        }
        
        // 遍历json数组
        // 相当于循环列表，获取到第一个json对象时，通过json.name输出name-key的值
        var jsonarr = [{"name":'alex',"age":20},{"name":'wxx',"age":30}];
        for(var k in jsonarr){
            console.log(jsonarr[k].name+' '+jsonarr[k].age);
        }

    </script>
</body>
</html>
```




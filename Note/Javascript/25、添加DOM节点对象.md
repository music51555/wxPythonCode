**document.createElement：**创建标签对象

**fatherobj.appendChild(childobj)：**添加子级节点

**fatherobj.removeChild：**删除子级节点

**fatherobj.insertBefore(新节点，参考节点)：**在指定标签前添加节点

从创建到销毁，页面性能是有损耗的，如果页面中频繁切换时，不要使用

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
    <button id="append">添加</button>
    <button id="remove">删除</button>
    <div id="box">	
        <h3 id="h3">这是一个h3的标题</h3>
    </div>
    <script type="text/javascript">
        window.onload = function(){
            function $(id){
                return document.getElementById(id);
            }

            // document.createElement('p')写为字符串
            var P_element = document.createElement('p');
            P_element.innerText = '这是一个大段落';

            $('append').onclick = function(){
                // 第一种添加子级的方式是fatherobj.append(childobj);
                $('box').appendChild(P_element);

                // 第二种添加子级的方式是fatherobj.insertBefore(newtagobj,oldtagobj);在已存在的节点对象前添加新的对象
                $('box').insertBefore(P_element,$('h3'));
            }
			
            //删除子级节点的方法是fatherobj.removeChild
            $('remove').onclick = function(){
                $('box').removeChild(P_element);
            }
        }
    </script>
</body>
</html>
```



**通过parentNode方法，获取父级对象**

**通过children方法，获取子级对象集合**

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
    <button id="append">添加</button>
    <button id="remove">删除</button>
    <div id="box">
        <h3 id="h3">这是一个h3的标题
            <span>小段落</span>
        </h3>
    </div>
    <script type="text/javascript">
        window.onload = function(){
            function $(id){
                return document.getElementById(id);
            }
            
            // 通过parentNode方法，获取父级对象
            var h3obj = document.getElementById('h3');
            boxparent = h3obj.parentNode;

            // 通过children方法，获取子级对象集合
            var divobj = document.getElementById('box');
            console.log(divobj.children);
            
            // 删除自己，通过parentNode找到自己的父级，再通过父级的children(this)/obj删除自己
            $('append').onclick = function(){
                this.parentNode.removeChild(this);
            }
        }
    </script>
</body>
</html>
```


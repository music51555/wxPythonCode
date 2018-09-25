快速，小巧，功能丰富的javascript库，分为编译版本和未编译版本，将未编译版本放在服务器上



**引入jQuery**

```html
<script type="text/javascript" src="./js/jquery-3.3.1.js"></script>
```



**在控制台打印JQuery**

```
>jQuery
ƒ ( selector, context ) {

		// The jQuery object is actually just the init constructor 'enhanced'
		// Need init if jQuery is called (just allow error to be thrown if not included)
		return new jQ…
```



其实是在jQuery文件中执行的这段源码，jQuery是一个全局函数

```javascript
version = "3.3.1",

	// jQuery的函数
	jQuery = function( selector, context ) {

		// return了一个新的jQuery对象
		return new jQuery.fn.init( selector, context );
	}

// 最后将对象赋值给window.jQuery和window.$，所以可以分别使用他们调用jQuery
if ( !noGlobal ) {
	window.jQuery = window.$ = jQuery;
}
```



jQuery的执行函数，function( selector, context )，按该格式调用

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>引入JQuery</title>
</head>
<body>
    <div class="box"></div>
    <script type="text/javascript" src="./js/jquery-3.3.1.js"></script>
    <script type="text/javascript">
        // 自执行函数，创建完即调用
        (function fn(){
            console.log('自执行函数');
        })();
        
        // 都表示jQuery对象
        console.log(jQuery);
        console.log($);

        // jQuery是一个全局函数，调用function( selector, context )，传入selector选择器和context，其中context是可以省略的，通过选择器查找对象
        // 返回jQuery.fn.init [div.box, prevObject: jQuery.fn.init(1)]
        console.log($('.box'));
    </script>
</body>
</html>
```


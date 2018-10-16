booststrap排版

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
            <div class="col-md-3">
                <!-- bootstarp分别为h1-h6、p设置了大小和样式 -->
                <h1>h1. Bootstrap heading</h1>
                <h2>h2. Bootstrap heading</h2>
                <h3>h3. Bootstrap heading</h3>
                <h4>h4. Bootstrap heading</h4>
                <h5>h5. Bootstrap heading</h5>
                <h6>h6. Bootstrap heading</h6>
                
                <!-- .lead类样式将凸显中心内容 -->
                <!-- .mark类样式将标记，内联文本元素,实则为文字添加的背景色 -->
                <p>Nullam quis risus eget urna mollis  <span class="lead">ornare</span> ornare vel eu leo. Cum sociis natoque penatibus et <mark>magnis dis parturient montes,</mark>  nascetur ridiculus mus. Nullam id dolor id nibh ultricies vehicula.</p>
            </div>
            
            <div class="col-md-3">
                <!-- del和s标签将内容添加删除线 -->
                <!-- ins标签标识插入的内容，以下划线展示内容 -->
                <p>Cum sociis <del>natoque penatibus</del>  et magnis dis parturient montes, nascetur ridiculus mus. Donec <s>ullamcorper nulla</s>  non metus auctor fringilla. Duis mollis, est non commodo luctus, nisi erat porttitor ligula, eget lacinia odio sem <ins>插入的内容</ins> nec elit. Donec ullamcorper nulla non metus auctor fringilla.</p>

                <!-- small标签将字体设置为小号字体 -->
                <small>小号字体展示</small>

                <!-- strong标签将字体着重显示，其实就是设置font-weight -->
                <strong>着重显示的字体</strong>

                <!-- em标签将内容以斜体展示 -->
                <em>斜体展示的内容</em>
            </div>
            
            <div class="col-md-3">
                <!-- text-xxxx对齐方式 -->
                <p class="text-left">Left aligned text.</p>
                <p class="text-center">Center aligned text.</p>
                <p class="text-right">Right aligned text.</p>
                <!-- 两端对齐 -->
                <p class="text-justify">Justified text.</p>
                <!-- 不换行对齐 -->
                <p class="text-nowrap">No wrap text.</p>

                <!-- 将内容变为大写 -->
                <p class="text-uppercase">hello world</p>
                <!-- 将内容变为小写 -->
                <p class="text-lowercase">hello world</p>
                <!-- 将首字母大写 -->
                <p class="text-capitalize">hello world</p>

                <!-- 缩略内容，title属性中展示缩略的完整内容 -->
                <abbr title="这是缩略内容">缩略</abbr>
            </div>
            
            <div class="col-md-3">
                <address>
                    <strong>北京市海淀区</strong><br>
                    <strong>北京市海淀区</strong>
                </address>
                <!-- blockquote块引用，在文字开头添加引用标识，实则是设置了border-left: 5px solid #eee -->
                <blockquote>
                    <p>这是引用内容</p>
                    <!-- 在blockquote中的footer将显示为以—开头，灰色的文字 -->
                    <footer>这是引用来源，在blockquote中的footer将显示为以—开头，灰色的文字 </footer>
                </blockquote>
            </div>
        </div>
        
        <div class="row">
            <div class="col-md-3">
                <ul>
                    <li>无序列表1</li>
                    <li>无序列表2</li>
                    <li>无序列表3</li>
                    <li>无序列表4</li>
                </ul>
                <ol>
                    <li>有序列表1</li>
                    <li>有序列表2</li>
                    <li>有序列表3</li>
                    <li>有序列表4</li>
                </ol>
                
                <!-- 列表中的每一行数据开头没有样式 -->
                <ul class="list-unstyled">
                    <li>无样式列表1</li>
                    <li>无样式列表2</li>
                    <li>无样式列表3</li>
                    <li>无样式列表4</li>
                </ul>
                
                <!-- 列表中的每一条数据在一行中显示 -->
                <ul class="list-inline">
                    <li>一行中显示1</li>
                    <li>一行中显示2</li>
                </ul>
            </div>
        </div>
    </div>
</body>
</html>
```


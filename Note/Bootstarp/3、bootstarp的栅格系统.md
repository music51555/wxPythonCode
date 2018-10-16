bootstarp栅格系统

**栅格系统**：通过一系列的行（row）与列（column）的组合来创建页面布局

要求：

1、`.row`必须包含在 `.container` （固定宽度）或 `.container-fluid` （100% 宽度）中 

```html
div class="container">
	<div class="row">

	</div>
</div>
```



2、在`row`中水平方向创建一组`column` ，内容放置于`column`内 

```html
div class="container">
	<div class="row">
        <div class="col-md-8">
            <div class="thumbnail">
                Bootstrap 提供了一套响应式、移动设备优先的流式栅格系统，随着屏幕或视口（viewport）尺寸的增加，系统会自动分为最多12列。它包含了易于使用的预定义类，还有强大的mixin 用于生成更具语义的布局。
            </div> 
        </div>
  
        <div class="col-md-4">
            <div class="thumbnail">
                Bootstrap 提供了一套响应式、移动设备优先的流式栅格系统，随着屏幕或视口（viewport）尺寸的增加，系统会自动分为最多12列。它包含了易于使用的预定义类，还有强大的mixin 用于生成更具语义的布局。
            </div> 
        </div>
    </div>
</div>
```



3、通过`col-lg- >=1200px大桌面显示器`、`col-md- >=992px桌面显示器`、`col-sm- >=768px平板屏幕`、`col-xs-  <768px手机屏幕`设置列的布局



4、堆叠到水平布局

```
col-xs-1...12个盒子堆叠
col-md-3...4个盒子堆叠
...
```



5、流式布局

最外层布局由container -->  .container-fluid，由banner中心宽度到100%全局宽度



6、多余的列将另起一行展示

```html
<div class="container">
    <div class="row">
        <!-- 在一行中无法容下9列+4列=13列的内容，所以将多余的列移动到下一行展示 -->
        <div class="col-md-9">
            <div class="thumbnail">
                Bootstrap 提供了一套响应式、移动设备优先的流式栅格系统，随着屏幕或视口（viewport）尺寸的增加，系统会自动分为最多12列。它包含了易于使用的预定义类，还有强大的mixin 用于生成更具语义的布局。
            </div>
        </div>
        <div class="col-md-4">
            <div class="thumbnail">
                Bootstrap 提供了一套响应式、移动设备优先的流式栅格系统，随着屏幕或视口（viewport）尺寸的增加，系统会自动分为最多12列。它包含了易于使用的预定义类，还有强大的mixin 用于生成更具语义的布局。
            </div>
        </div>
    </div>
</div>
```



7、列偏移

当一行12列中，只有2个盒子，如何对称排列在需要偏移的盒子添加类`col-offset-md-4`，表示偏移4列

```html
<div class="container">
    <div class="row">
        <div class="col-md-4 ">.col-xs-6 .col-sm-3</div>
        <div class="col-md-4 col-md-offset-4">.col-xs-6 .col-sm-3</div>
    </div>
</div>
```





8、嵌套列

在一个列盒子中添加row，在row中继续添加列

```html
<div class="container">
    <div class="row">
        <div class="col-md-4 ">
            <div class="row">
                <div class="col-md-4">
                    <div class="thumbnail">
                        一个盒子
                    </div>
                </div>
                <div class="col-md-4">
                    <div class="thumbnail">
                        一个盒子
                    </div>
                </div>
                <div class="col-md-4">
                    <div class="thumbnail">
                        一个盒子
                    </div>
                </div>
            </div>
        </div>
        <div class="col-md-4">
            <div class="thumbnail">
                一个盒子
            </div>
        </div>
        <div class="col-md-4">
            <div class="thumbnail">
                一个盒子
            </div>
        </div>
    </div>
</div>
```



9、列排序

```html
<div class="row">
    <!-- push是将后面的盒子推到后面，pull是将后面的盒子拉到前面，调换了顺序 -->
    <div class="col-md-9 col-md-push-3">.col-md-9 .col-md-push-3</div>
    <div class="col-md-3 col-md-pull-9">.col-md-3 .col-md-pull-9</div>
</div>
```




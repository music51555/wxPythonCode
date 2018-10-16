bootstarp表格

1、基本表格

为表格添加.table类



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
                <!-- table-responsive  响应的；应答的 美 /rɪ'spɑnsɪv/ 表示当页面展示区域缩小到比表格宽度小时，会为当前表格增加滚动条，该类放置在包裹表格的外层 -->
                <div class="thumbnail table-responsive">
                    <!-- table 类实现表格的基本样式展示 ，为每一行数据增加一条横线-->
                    <!-- table-striped  美 /'straɪpɪd/ 类为表格使用nth-child选择其实现添加条纹背景色的样式 -->
                    <!-- table-bordered 为表格的每一列也附加了边框 -->
                    <!-- table-hover 当鼠标悬浮在表格中会为当前行的数据添加背景色 -->
                    <!-- table-condensed  美 /kən'dɛnst/表示缩紧表格的每一行数据-->
                    <table class="table table-striped table-bordered table-hover table-condensed">
                        <!--  五种状态分别为active、success、info、warning、danger，每一种状态都是一种颜色 -->
                        <tr class="active">
                            <td>id</td>
                            <td>name</td>
                            <td>age</td>
                        </tr>
                        <tr class="success">
                            <td>1</td>
                            <td>alex</td>
                            <td>18</td>
                        </tr>
                        <tr class="info">
                            <td>2</td>
                            <td>wxx</td>
                            <td>28</td>
                        </tr>
                        <tr class="warning">
                            <td>3</td>
                            <td>egon</td>
                            <td>38</td>
                        </tr>
                        <tr class="danger">
                            <td>4</td>
                            <td>xiaomaxiaomaxiaomaxiaomaxiaomaxiaomaxiaomaxiaomaxiaomaxiaomaxiaomaxiaomaxiaomaxiaoma</td>
                            <td>48</td>
                        </tr>
                    </table>
                </div>
            </div>
        </div>
    </div>
</body>
</html>
```


常用标签

标题标签：

heading

不要用标题标签改变同一行中的字体大小，使用css来定义

用于文章和网站的标题

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <title>Page Title</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" type="text/css" media="screen" href="main.css" />
    <script src="main.js"></script>
</head>
<body>
    <!-- div标签，盒子标签，在页面中看不到效果，在父级区的div层级中，包含了4个区div，div标签是块级元素，每块独占一行 -->
    <!-- id和class都是给区域起名字，id在文档中是唯一的，多用于js，class是可以重名的，多用于CSS -->
    <div id="warp">
        <div class="heading">
            <!-- heading 标题h1-h6 ，没有h7，标题会自动换行，块级元素，独占一行，可以设置宽高，不设置时是浏览器默认宽度，style表示添加样式-->
            <h1 style="height:2000px">百度一下</h1>

            <h2>百度一下</h2>
            <h3>百度一下</h3>
            <h4>百度一下</h4>
            <!-- id="p5"表示为当前标题的区域标识为p5 -->
            <h5 style="height:2000px" id="p5">百度一下</h5>
            <h6>百度一下</h6>
        </div>

        <div class="p1">
            <!-- <b>表示加粗字体</b> 而 <strong>表示强调重要性，一般使用<strong>...</strong>-->
            <!-- <i>表示斜体显示</i> -->
            <!-- <u>表示下划线</u> -->	
            <!-- <sup>表示上标</sup>，<sub>表示下标</sub> -->
            <p>2<sup>2</sup>黄河路街道的<b>爱琴家政</b>，<strong>大家而熟能详</strong>，<i>今天我们就走进</i>这个家政大家庭自<u>2001年</u>以来，爱琴家政为我社区也<s>添加</s>增添了不少光彩，爱琴大姐秉承服务于民，手爱于民的宗旨，在我社区举办了很多大型的义工工作劳动</p>
            
            <!-- 分割线标签 hr -->
            <hr>

            <!-- 段落标签 paragraph， 美 /'pærəɡræf/  独占一行，块级元素，样式和普通文本一样-->
            <!-- 换行标签 br -->
            <!-- span标签，行内标签，把一段内容中标注出来，单独通过css来修改，如果不对 span 应用样式，那么 span 元素中的文本与其他文本不会任何视觉上的差异 -->
            <p>这是一个段落标签<span>这是一个</span>段落标签这是一个段落<br>标签这是一个段落标签这是一个段落标签这是一个段落标签</p>
        </div>

        <div class="anchor">
            <!-- 超链接 ，anchor 美 /'æŋkɚ/  锚；抛锚停泊-->
            <!--target属性表示当前页target="_self"，还是新的标签页target="_blank"打开网页-->
            <!-- title表示鼠标放置在链接上，所显示的标题 -->
            <a href="https://www.baidu.com" target="_blank" title="走向百度">百度一下</a>
            
            <!-- a标签是行内标签，无法设置宽高。点击链接后，将会下载指定的压缩包文件 -->
            <a href="./a.zip">点击下载压缩包</a>

            <!-- 邮箱，如果电脑上配置了如outlook等，就会自动打开 -->
            <a href="lelevipforever@sina.com">与我联系</a>
            
            <!-- 跳转到顶部，点击后将跳转到浏览器顶部，写为#号时是跳转到浏览器顶部-->
            <!-- 当设置一块标题的区域id为p5时，点击后跳转到对应的区域-->
            <a href="#p5">跳转到顶部</a>

            <!-- 表示为a标签添加一个javascript脚本动作，当只设置为href="javascript:"时是没有动作的 -->
            <a href="javascript:alert(1)">执行脚本</a>
        </div>

        <div class="list">
            <!-- unordered list无需列表 ul标签和li标签相关联，默认前面显示一个实心圆 -->
            <!-- 如果想要修改序号，需要使用type属性,circle表示一个空心圆，square表示一个实心方块，none表示不显示标识 -->
            <!-- 空格&nbsp和尖括号&gt;等 -->
            <ul type="square">
                <li>我的账户&nbsp;&nbsp;&nbsp;&nbsp;&gt;</li>
                <li>我的订单&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&gt;</li>
                <li>我的优惠卷&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&gt;</li>
                <li>我的收藏&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&gt;</li>
                <li>退出&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&gt;</li>
            </ul>

            <!-- ordered list有序列表 -->
            <!-- 如果想要修改序号，需要使用type属性，默认以数字序号排序，1表示数字序号，a、A分别表示大小写字母,i和I分别表示大小写罗马字符 -->
            <ol type="i">
                <li>我的账户></li>
                <li>我的订单></li>
                <li>我的优惠卷></li>
                <li>我的收藏></li>
                <li>退出></li>
            </ol>
        </div>

        <!-- 图片标签 img，格式png,jpg,gif，图片可以是本地的，也可以是网络的，可以在style属性中设置宽高，行内快元素，可以设置宽高-->
        <!--将图片放置在a标签中，可以达到将图片设置为链接的效果-->
        <!-- alt可以设置图片加载失败后显示的图片的文字描述信息 -->
        <div class="image">
            <div class="python">
                <a href="http://www.baidu.com" target="_blank" title="python">
                    <img src="./homesmall1.png" alt="" style="width:600px;height:300px"/>
                </a>
            </div>
            <div class="linux">
            <img src="./homesmall2.png" alt="" style="width:600px;height:300px">
            </div>
        </div>
        
        <!-- 表格 table块级元素，由thead，tbody，tfoot三部分组成 -->
        <div class="table">
        	<!-- 在table标签添加border="1" cellspacing="0"，分别表示边框的粗细，和表格间的空隙 -->
            <table border="1" cellspacing="0">
                <thead>
                    <tr>
                  <!-- 在head中是使用th添加数据，这会将该行数据加粗显示-->
                  <!-- 如果在thead标签中只有一个th，并且在这行数据中使用了colspan，那么会居中显示 -->
                        <th></th>
                        <th>星期一</th>
                        <th>星期二</th>
                        <th>星期三</th>
                        <th>星期四</th>
                        <th>星期五</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <!-- 将行合并，rowspan -->
                        <td rowspan="3">上午</td>
                        <!-- 在body是使用td添加数据 -->
                        <td>语文</td>
                        <td>数学</td>
                        <td>英语</td>
                        <td>物理</td>
                        <td>化学</td>
                    </tr>
                    <tr>
                        <td>语文</td>
                        <td>数学</td>
                        <td>英语</td>
                        <td>物理</td>
                        <td>化学</td>
                    </tr>
                    <tr>
                        <td>语文</td>
                        <td>数学</td>
                        <td>英语</td>
                        <td>物理</td>
                        <td>化学</td>
                    </tr>
                    <tr>
                        <td rowspan="2">下午</td>
                        <td>语文</td>
                        <td>数学</td>
                        <td>英语</td>
                        <td>物理</td>
                        <td>化学</td>
                    </tr>
                    <tr>
                        <td>语文</td>
                        <td>数学</td>
                        <td>英语</td>
                        <td>物理</td>
                        <td>化学</td>
                    </tr>
                </tbody>
                <tfoot>
                    <tr>
                        <!-- 将列合并，colspan -->
                        <!-- 在tfoot中也是使用td添加数据 -->
                        <td colspan="6">课程表</td>
                    </tr>
                </tfoot>
            </table>
        </div>  

    </div>
</body>
</html>
```


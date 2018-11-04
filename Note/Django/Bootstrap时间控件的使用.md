Bootstrap时间控件的使用

在http://www.bootcss.com/p/bootstrap-datetimepicker/index.htm下载zip包

引入

```html
<link rel="stylesheet" href="/static/bootstrap-3.3.7/css/bootstrap.css">
<link rel="stylesheet" href="/static/datetimepicker/css/bootstrap-datetimepicker.css">
<script type="text/javascript" src="/static/jquery-3.3.1.js"></script>
<script type="text/javascript" src="/static/bootstrap-3.3.7/js/bootstrap.js"></script>
<script type="text/javascript" src="/static/datetimepicker/js/bootstrap-datetimepicker.js"></script>
<script type="text/javascript" src="/static/datetimepicker/js/locales/bootstrap-datetimepicker.fr.js"></script>
```

HTML

```html
<input type="text" class="form-control form_datetime" id="addtime" name="addtime" value="{{ now }}" placeholder="">
```

JQuery

```html
$('.form_datetime').datetimepicker({
    minView: "month", //选择日期后，不会再跳转去选择时分秒
    language: 'zh-CN',
    format: 'yyyy-mm-dd',
    todayBtn: 1,
    autoclose: 1,
});
```



或直接使用input的type=date
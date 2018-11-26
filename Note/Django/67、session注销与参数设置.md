session注销

del request.session[key]

request.session.fulsh()

代码实现是：

1、获取sessionid的cookie值：session_key

2、通过session_key在django_session表中过滤数据，并删除

3、删除sessionid的cookie值：delete_cookie
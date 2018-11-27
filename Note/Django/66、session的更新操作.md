session的更新操作：

浏览器第一次访问服务器，如果登录成功，则设置session信息：

```python
if user_obj:
	request.session['is_login']=True
	request.session['username']=user_obj.username
```

浏览器生成了`sessionid`的`cookie`信息，存储的是`session_key:10lho0q4plosk2r41phad7c2bsxb7si8`，同时在`django_session`表中对应`session_data:{'login':True,'username':'alex'}` 

![1543221993540](.\images\生成sessionid)

**所以，**切换用户登录后，如果当前浏览器的`cookie`中已经存在`sessionid`的`cookie`信息，那么就会在`django_session`表中按`session_key`完全更新`session_data`，而不是再新建一条`session`信息

**但是，**更换浏览器后登录，浏览器中没有`sessionid`的`cookie`信息，就会在`django_session`表中插入一条新的记录


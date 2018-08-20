sql注入

```python
#通过添加双引号，和注释-- 来截断sql语句，达到sql注入的效果，使得只查询出了用户名后，就被-- 注释了后面授权查询语句
user:wangxin" -- nihao
password:
select * from userinfo where username="wangxin" -- nihao" and password=""
登录成功
```



```python
#或是通过添加双银后，和or 1=1的条件，来达到sql注入的效果
user:wangxin" or 1=1 -- haha
password:
select * from userinfo where username="wangxin" or 1=1 -- haha" and password=""
登录成功
```



所以不适用“ ”来拼接sql语句，直接使用cursor.execute(sql,username,password)来实现传递参数

```python
#在cursor.execute(sql,在此传入元祖类型的数据(username,password))来实现传参
cursor=conn.cursor()
sql='select * from userinfo where username=%s and password=%s'
rows=cursor.execute(sql,(username,password))
```


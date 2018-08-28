**插入记录**

```python
import pymysql

conn=pymysql.connect(
    host='140.143.188.59',
    port=3306,
    user='wanghai',
    password='123456',
    db='db1',
    charset='utf8'
)

#获取到mysql>_游标
cursor=conn.cursor()

sql='insert into userinfo(username,password) values(%s,%s);'
rows=cursor.execute(sql,('alex','123456'))

#5，查询当前表中的最后一行rowid是多少
#1、必须在cursor.execute()方法后执行
#2、必须在insert into语句后使用，才能正确查询出行id，select语句后显示为None
print(cursor.lastrowid)

#执行insert和update语句后，还需要使用conn.commit提交数据，发现只有在insert插入数据后才能显示lastrowid的值
conn.commit()

#关闭游标
cursor.close()
#关闭数据库连接
conn.close()

#成功插入记录
'''
mysql> select * from userinfo;
+----+----------+----------+
| id | username | password |
+----+----------+----------+
|  1 | wangxin  | 123456   |
|  2 | peiqi    | 123      |
|  3 | alex     | 123456   |
+----+----------+----------+
'''
```



**插入多条记录**

```python
cursor=conn.cursor()

sql='insert into userinfo(username,password) values(%s,%s);'
#由cursor.execute改为cursor.executemany()，并将数据以元祖的形式存储在列表中
rows=cursor.executemany(sql,[('egon','123456'),('daniu','123456'),('lifei','123')])

conn.commit()

print(cursor.lastrowid)

#插入了多条记录
'''
mysql> select * from userinfo;
+----+----------+----------+
| id | username | password |
+----+----------+----------+
|  1 | wangxin  | 123456   |
|  2 | peiqi    | 123      |
|  3 | alex     | 123456   |
|  5 | alex     | 123456   |
|  6 | egon     | 123456   |
|  7 | daniu    | 123456   |
|  8 | lifei    | 123      |
+----+----------+----------+
'''
```



**查询记录**

**取出一条记录**

```python
import pymysql

conn=pymysql.connect(
    host='140.143.188.59',
    port=3306,
    user='wanghai',
    password='123456',
    db='db1',
    charset='utf8'
)

cursor=conn.cursor()

sql='select * from userinfo'
rows=cursor.execute(sql)

#通过fetchone从管道中取出一条数据,美 /fɛtʃ/  取来，取出
print(cursor.fetchone())

cursor.close()
conn.close()
'''
(1, 'wangxin', '123456')
'''
```



**取出多条记录**

```python
cursor=conn.cursor()

sql='select * from userinfo'
rows=cursor.execute(sql)

#通过fetchmany方法取出多条记录，默认为1条，查询的结果是元祖类型
print(cursor.fetchmany(2))
```



**取出所有记录**

```python
cursor=conn.cursor()

sql='select * from userinfo'
rows=cursor.execute(sql)

#通过fetchall方法取出所有数据，结果使元祖类型，所以for循环展示所有数据
for i in cursor.fetchall():
    print(i)
    
'''
(1, 'wangxin', '123456')
(2, 'peiqi', '123')
(3, 'alex', '123456')
(5, 'alex', '123456')
(6, 'egon', '123456')
(7, 'daniu', '123456')
(8, 'lifei', '123')
'''
```



**根据绝对位置移动游标**

```python
cursor=conn.cursor()
sql='select * from userinfo'
rows=cursor.execute(sql)
for i in cursor.fetchall():
    print(i)

#取完数据后再取数据，就会得到一个空的元祖，所以可以像文件的seek一样，使用cursor.scroll(x，mode)方法，可以调整光标位置，当mode为'absolute'时，是相对绝对位置调整光标，如调整到第1行，第2行等
cursor.scroll(0,mode='absolute')
print(cursor.fetchone())

#取完数据，根据绝对位置调整游标至表头，再通过fetchone()取得第一条数据
'''
(1, 'wangxin', '123456')
(2, 'peiqi', '123')
(3, 'alex', '123456')
(5, 'alex', '123456')
(6, 'egon', '123456')
(7, 'daniu', '123456')
(8, 'lifei', '123')
(1, 'wangxin', '123456')
'''
```



**根据相对位置移动游标**

```python
cursor=conn.cursor()
sql='select * from userinfo'
rows=cursor.execute(sql)

print(cursor.fetchone())
#读取一条数据后，根据当前位置，调整游标后再读取数据
cursor.scroll(1,mode='relative')
print(cursor.fetchone())

'''
(1, 'wangxin', '123456')
(3, 'alex', '123456')
'''
```



**以字典的形式读取结果**

```python
#配置光标项，改为用字典的形式查看结果
cursor=conn.cursor(pymysql.cursors.DictCursor)
sql='select * from userinfo'
rows=cursor.execute(sql)

print(cursor.fetchone())
cursor.scroll(1,mode='relative')
print(cursor.fetchone())

'''
{'id': 1, 'username': 'wangxin', 'password': '123456'}
{'id': 3, 'username': 'alex', 'password': '123456'}
'''
```


安装pymysql模块

```python
import pymysql

username=input('user:')
password=input('password:')

#在连接前需要创建远程账号
#grant all on *.* to 'xiaoyue'@'%' identified by "123";授权并创建了账号
conn=pymysql.connect(
    host='140.143.188.59',
    port=3306,
    user='xiaoyue',
    password='123',
    db='db1',
    charset='utf8'
)

#获取到mysql命令行待输入sql语句的光标，美 /'kɝsɚ/ 光标
cursor=conn.cursor()

#sql语句，注意username="%s" and password="%s"一定要用引号括起来
#连接信息定义了数据库，则不用再写为数据库.表名
sql='select * from userinfo where username="%s" and password="%s"'%(username,password)

#执行sql语句后影响的行数，如果有结果则if rows为True，反之False
rows=cursor.execute(sql)

#关闭光标和关闭本次数据库的连接
cursor.close()
conn.close()

if rows:
    print('登录成功')
else:
    print('登录失败')

'''
mysql> select * from db1.userinfo;
+------+----------+----------+
| id   | username | password |
+------+----------+----------+
|    1 | wangxin  | 123456   |
|    2 | peiqi    | 123      |
+------+----------+----------+

user:wangxin
password:123456
登录成功
'''
```


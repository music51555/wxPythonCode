import pymysql

username=input('user:')
password=input('password:')

conn=pymysql.connect(
    host='140.143.188.59',
    port=3306,
    user='xiaoyue',
    password='123',
    db='db1',
    charset='utf8'
)

cursor=conn.cursor()
sql='select * from userinfo where username=%s and password=%s'
rows=cursor.execute(sql,(username,password))

cursor.close()
conn.close()

if rows:
    print('登录成功')
else:
    print('登录失败')
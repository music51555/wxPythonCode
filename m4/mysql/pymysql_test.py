import pymysql

conn=pymysql.connect(
    host='140.143.188.59',
    port=3306,
    user='wanghai',
    password='123456',
    db='db1',
    charset='utf8'
)

cursor=conn.cursor(pymysql.cursors.DictCursor)
cursor.callproc('p1')
res=cursor.fetchall()
print(res)

cursor.close()
conn.close()
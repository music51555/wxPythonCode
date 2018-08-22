import pymysql

conn = pymysql.connect(
    host='140.143.188.59',
    port=3306,
    user='wanghai',
    password='123456',
    db='db1',
    charset='utf8'
)

cursor=conn.cursor(pymysql.cursors.DictCursor)
sql='select * from userinfo'
cursor.callproc('p2',(2,4,0))
res = cursor.fetchall()
print(res)
cursor.execute('select @_p2_2')
print(cursor.fetchone())

cursor.close()
conn.close()
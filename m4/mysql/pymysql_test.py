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
#存储方式其实是@_p2_0=2,@_p2_1=4,@_p2_2=0
cursor.callproc('p2',(2,4,0))
print(cursor.fetchall())
cursor.execute('select @_p2_2')
print(cursor.fetchone())


cursor.close()
conn.close()
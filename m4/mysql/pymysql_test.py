import pymysql

conn = pymysql.connect(
    host='140.143.188.59',
    port=3306,
    user='wanghai',
    password='123456',
    db='m4exam',
    charset='utf8'
)

cursor=conn.cursor(pymysql.cursors.DictCursor)
cursor.callproc('p3',(2,12,1))
res=cursor.fetchall()
print(res)

cursor.execute('select @_p3_2')
res=cursor.fetchone()
print(res)

cursor.close()
conn.close()
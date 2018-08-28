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
sql='select * from student'
cursor.execute(sql)
res = cursor.fetchmany(2)
print(res)

cursor.scroll(0,mode='relative')
res = cursor.fetchone()
print(res)

cursor.close()
conn.close()
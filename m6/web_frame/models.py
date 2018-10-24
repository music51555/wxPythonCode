import pymysql

conn = pymysql.connect(
    host = '140.143.132.118',
    port = 3306,
    user = 'xiaoxin',
    password = 'Nishi458_2',
    db = 'm6',
    charset = 'utf8'
)

cursor = conn.cursor()
sql = 'create table userinfo(id int primary key,name varchar(20),pwd varchar(20))'
cursor.execute(sql)
conn.commit()
cursor.close()
conn.close()


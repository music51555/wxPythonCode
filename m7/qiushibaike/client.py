import pymysql

conn = pymysql.connect(
    host='140.143.132.118',
    port=3306,
    user='xiaoxin',
    password='Nishi458_2',
    db='blog',
    charset='utf8'
)

from django.urls import path,re_path,include,reverse
from django.shortcuts import render,HttpResponse,redirect

cursor = conn.cursor()

sql = 'select username from blog_userinfo where username = %s'

ret = cursor.execute(sql,('alex'))
print(cursor.fetchone())
print(cursor.fetchall())

sql = 'insert into user(id, name) values(%s,%s)'

ret = cursor.executemany(sql, [(1,'alex'),(2,'wangxin')])
conn.commit()



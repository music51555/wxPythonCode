**where**

```mysql
#单条件
select * from employee where id > 7

#多条件，查找出职位是老师，薪资大于8000的老师
mysql> select id,name from employee where post='teacher' and salary>8000;
+----+------------+
| id | name       |
+----+------------+
|  2 | alex       |
|  3 | wupeiqi    |
|  6 | jingliyang |
|  7 | jinxin     |
|  8 | 成龙       |
+----+------------+

#薪资大于等于20000，小于等于30000
mysql> select id,name from employee where salary>=20000 and salary<=30000;
+----+-----------+
| id | name      |
+----+-----------+
|  7 | jinxin    |
| 15 | 程咬金    |
+----+-----------+
#简写为between...and...，表示大于等于xxx且小于等于xxx
mysql> select id,name from employee where salary between 20000 and 30000;
+----+-----------+
| id | name      |
+----+-----------+
|  7 | jinxin    |
| 15 | 程咬金     |
+----+-----------+

#薪资小于20000，或大于30000
mysql> select id,name,salary from employee where salary<20000 or salary > 30000;
+----+------------+------------+
| id | name       | salary     |
+----+------------+------------+
|  1 | egon       |    7300.33 |
|  2 | alex       | 1000000.31 |
|  3 | wupeiqi    |    8300.00 |
|  4 | yuanhao    |    3500.00 |
|  5 | liwenzhou  |    2100.00 |
|  6 | jingliyang |    9000.00 |
#简写为取反,通过not关键字取反
mysql> select id,name,salary from employee where salary not between 20000 and 30000;
+----+------------+------------+
| id | name       | salary     |
+----+------------+------------+
|  1 | egon       |    7300.33 |
|  2 | alex       | 1000000.31 |
|  3 | wupeiqi    |    8300.00 |
|  4 | yuanhao    |    3500.00 |
|  5 | liwenzhou  |    2100.00 |

#in，取年龄在。。之间的
mysql> select id,name,salary from employee where age in (81,78);
+----+---------+------------+
| id | name    | salary     |
+----+---------+------------+
|  2 | alex    | 1000000.31 |
|  3 | wupeiqi |    8300.00 |
+----+---------+------------+

#is Null和is not Null
mysql> select * from employee where post_comment is Null;
mysql> select * from employee where post_comment is not Null;

#like模糊匹配，%百分号表示任意多个字符
mysql> select id,name from employee where name like 'jin%';
+----+------------+
| id | name       |
+----+------------+
|  6 | jingliyang |
|  7 | jinxin     |
+----+------------+

#_下划线表示任意一个字符
mysql> select id,name from employee where name like 'jin___';
+----+--------+
| id | name   |
+----+--------+
|  7 | jinxin |
+----+--------+
```



正则表达式查询

**regexp关键字，使用了regexp，就无需like关键字，使其一即可**

```mysql
#添加regexp关键字，支持正则表达式
mysql> select id,name,age from employee where name regexp '^jin';
+----+------------+-----+
| id | name       | age |
+----+------------+-----+
|  6 | jingliyang |  18 |
|  7 | jinxin     |  18 |
+----+------------+-----+

#查找以jin开头，以g或n结尾的内容
mysql> select id,name,age from employee where name regexp '^jin.*(g|n)';
+----+------------+-----+
| id | name       | age |
+----+------------+-----+
|  6 | jingliyang |  18 |
|  7 | jinxin     |  18 |
+----+------------+-----+
```


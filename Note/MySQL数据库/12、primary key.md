primary key

对于innodb存储引擎，一张表中必须有一个主键，不为空，且唯一，如果没有设置主键，那么就会对每一条记录生成rowid作为主键



**单列主键**

使用primary key关键字设置主键，id字段一般情况下设置为主键

```python
create table t1(id int primary key,name char(5));

#设置主键后，Key字段被写为PRI，且不允许为空，表示primary key主键
mysql> desc t1;
+-------+---------+------+-----+---------+-------+
| Field | Type    | Null | Key | Default | Extra |
+-------+---------+------+-----+---------+-------+
| id    | int(11) | NO   | PRI | NULL    |       |
| name  | char(5) | YES  |     | NULL    |       |
+-------+---------+------+-----+---------+-------+

mysql> select * from t1;
+----+-------+
| id | name  |
+----+-------+
|  1 | alex  |
|  2 | peiqi |
+----+-------+
2 rows in set (0.00 sec)

#如果在主键中插入重复的数据会报错
mysql> insert into t1 values(2,'wxx');
ERROR 1062 (23000): Duplicate entry '2' for key 'PRIMARY'
    
#如果没有插入主键值，且没有为主键设置默认值的话，会报错
mysql> insert into t1(name) values('wanghai');
ERROR 1364 (HY000): Field 'id' doesn't have a default value
    
#如果设置了主键的默认值，那么在没有传入主键的情况下，会默认使用默认值
mysql> desc t1;
+-------+---------+------+-----+---------+-------+
| Field | Type    | Null | Key | Default | Extra |
+-------+---------+------+-----+---------+-------+
| id    | int(11) | NO   | PRI | 0       |       |
| name  | char(5) | YES  |     | NULL    |       |
+-------+---------+------+-----+---------+-------+

insert into t1(name) values('wxx');

mysql> select * from t1;
+----+-------+
| id | name  |
+----+-------+
|  0 | wxx   |
|  1 | alex  |
|  2 | peiqi |
+----+-------+
```



如果没有指定主键，会查找一个not null、unique的列为主键

```python
mysql> create table t2(id int not null unique,name char(5));

#没有设置主键，但设置了id字段不为空，且是唯一的，所以innodb类型的表会默认查找一个not null、unique的列为主键
mysql> desc t2;
+-------+---------+------+-----+---------+-------+
| Field | Type    | Null | Key | Default | Extra |
+-------+---------+------+-----+---------+-------+
| id    | int(11) | NO   | PRI | NULL    |       |
| name  | char(5) | YES  |     | NULL    |       |
+-------+---------+------+-----+---------+-------+
```



**复合主键**

联合唯一

```python
create table t3(id int,name char(5),host char(15),port char(4),primary key(host,port));

mysql> desc t3;
+-------+----------+------+-----+---------+-------+
| Field | Type     | Null | Key | Default | Extra |
+-------+----------+------+-----+---------+-------+
| id    | int(11)  | YES  |     | NULL    |       |
| name  | char(5)  | YES  |     | NULL    |       |
| host  | char(15) | NO   | PRI |         |       |   #设置的联合主键都被显示为PRI主键
| port  | char(4)  | NO   | PRI |         |       |
+-------+----------+------+-----+---------+-------+

#正常插入数据，host和port端口联合唯一，且不为空
mysql> select * from t3;
+------+------+---------------+------+
| id   | name | host          | port |
+------+------+---------------+------+
|    2 | sub  | 192.168.0.151 | 8090 |
|    1 | main | 192.168.0.5   | 8080 |
+------+------+---------------+------+

#插入重复的数据
mysql> insert into t3 values(3,'sub1','192.168.0.151','8090');
ERROR 1062 (23000): Duplicate entry '192.168.0.151-8090' for key 'PRIMARY'
```


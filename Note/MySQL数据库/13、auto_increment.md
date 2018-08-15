auto_increment

**自增长**

```mysql
#在数据类型后添加auto_increment使列变为自增长列，美 /'ɪŋkrəmənt/ 增量；增加
mysql> create table t4(id int primary key auto_increment,name char(5));

mysql> desc t4;
+-------+---------+------+-----+---------+----------------+
| Field | Type    | Null | Key | Default | Extra          |
+-------+---------+------+-----+---------+----------------+
| id    | int(11) | NO   | PRI | NULL    | auto_increment |
| name  | char(5) | YES  |     | NULL    |                |
+-------+---------+------+-----+---------+----------------+
```



在设置自增的列时，如果该列不是一个key，那么就会报错，目前所学的key是unique和primary key

```mysql
mysql> create table t4(id int auto_increment,name char(5));
ERROR 1075 (42000): Incorrect table definition; there can be only one auto column and it must be defined as a key
```



设置列为自增长后，可以不用插入指定的列值，会根据数据类型自动增长数值

```mysql
mysql> insert into t4(name) values('alex'),('peiqi'),('wxx');

mysql> select * from t4;
+----+-------+
| id | name  |
+----+-------+
|  1 | alex  |
|  2 | peiqi |
|  3 | wxx   |
+----+-------+
```



但是，如果插入了自增长的值，那么在下一次插入数据时，将根据最后的数值大小自增长

```mysql
#最后的序号变为7
mysql> insert into t4 values(7,'hai');

#所以再次插入数据时，自动增长为序号8
mysql> insert into t4(name) values('mary');
mysql> select * from t4;
+----+-------+
| id | name  |
+----+-------+
|  1 | alex  |
|  2 | peiqi |
|  3 | wxx   |
|  7 | hai   |
|  8 | mary  |
+----+-------+
```



**设置起始序号，和步长**

**查看mysql自定义的变量**

```python
mysql> show variables;
```



通过%，查找某个变量

```mysql
mysql> show variables like 'auto_increment%';
+--------------------------+-------+
| Variable_name            | Value |
+--------------------------+-------+
| auto_increment_increment | 1     |    #表示步长，表示每一次间隔多少序号插入数据
| auto_increment_offset    | 1     |    #表示偏移起始位置，如第一次插入数据时的起始序号
+--------------------------+-------+
```



**设置步长**

session表示在本次会话中起作用，global表示全局设置

```mysql
#设置步长
mysql> set session auto_increment_increment=5;

mysql> insert into t4(name) values('hong');

#设置步长后，再次插入数据时，将以间隔的步长插入序号，而间隔的序号，是以序号1开始计算的，
mysql> select * from t4;
+----+-------+
| id | name  |
+----+-------+
|  1 | alex  |
|  2 | peiqi |
|  3 | wxx   |
|  7 | hai   |
|  8 | mary  |
| 11 | hong  |    #序号11是根据序号1开始计算的1--6--11
| 16 | hong  |
| 21 | hong  |
+----+-------+
```



**设置起始偏移量**

表示第一插入数值的起始序号，起始偏移量必须小于步长，

```mysql
#设置起始偏移量
mysql> set session auto_increment_offset=3;

#插入数据后，起始序号变为从设置的3开始，并按照步长插入数据
insert into t4(name) values('alex'),('peiqi');
mysql> select * from t4;
+----+-------+
| id | name  |
+----+-------+
|  3 | alex  |
|  8 | peiqi |
+----+-------+
```





**清空表**

如果使用delete from table清空表，这样是没有清空序号索引的起始位置的

```mysql
mysql> delete from t4;

#如果通过delete from table清空表的话，那么自增的步长序号没有归0，AUTO_INCREMENT=13
mysql> show create table t4;

| t4    | CREATE TABLE `t4` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` char(5) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8 |
```



使用truncate table来清空表，使其回到最初始的状态

```mysql
truncate t4;

| t4    | CREATE TABLE `t4` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` char(5) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 |
```


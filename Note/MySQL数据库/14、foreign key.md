foreign key：建立表之间的关系

**外键的意义：**

建立员工表，员工表包含id、name、sex、department字段，可能遇到的问题是有多个员工隶属于同一个部门，员工的department字段，都有类似“技术指导中心”这样的描述，**重复的显示了冗余的信息**

```mysql
mysql> select * from staff_info;
+------+-------+--------+--------------------+
| id   | name  | sex    | department         |
+------+-------+--------+--------------------+
|    1 | alex  | male   | 技术指导中心        |
|    2 | peiqi | male   | 市场宣传中心        |
|    3 | bill  | male   | 财务管理中心        |
|    4 | fang  | female | 技术指导中心        |
|    5 | hai   | male   | 市场宣传中心        |
+------+-------+--------+--------------------+
```



建立部门表，部门表包含id、name，description字段，所以可以使用部门表的id字段作为员工表department列的外键，用来区分员工隶属于哪个部门

```mysql
mysql> select * from department;
+------+--------+--------------------+
| id   | name   | description        |
+------+--------+--------------------+
|    1 | 技术   | 技术研发中心        |
|    2 | 市场   | 市场宣传中心        |
|    3 | 财务   | 财务管理中心        |
+------+--------+--------------------+
```



最终想要的简化结果

```mysql
mysql> select * from staff_info;
+------+-------+--------+------------+
| id   | name  | sex    | department |
+------+-------+--------+------------+
|    1 | alex  | male   | 1          | #技术研发中心
|    2 | peiqi | male   | 2          | #市场宣传中心
|    3 | bill  | male   | 3          | #财务管理中心
|    4 | fang  | female | 1          |
|    5 | hai   | male   | 2          |
+------+-------+--------+------------+
```



**外键的创建过程**

**1、先建立被关联的表（部门表）**

要保证被关联的表的外键列，是唯一的，unique或是主键

```mysql
 #先创建被关联的部门表，因为在创建关联员工表的外键时，会references被关联表及其关联列，否则会提示表不存在
 create table department(
	id int primary key,
	name char(5),
	description char(20)
);
```



**2、再建立关联的表（员工表）**

表示员工表的dep_id作为员工表的外键

```mysql
create table staff_info(
	id int,
	name char(5),
	sex enum('male','female'),
	dep_id int,
	foreign key(dep_id) references department(id)
);
```



**插入数据**

关联表中的外键在插入数据时，要保障被关联表中已存在的对应的内容，所以先插入被关联表中的数据

```mysql
#先插入被关联表的数据，保证了被关联表中的数据是存在的
insert into department values
(1,'技术','技术指导中心'),
(2,'市场','市场运营中心'),
(3,'财务','财务管理中心');

mysql> select * from department;
+----+--------+--------------------+
| id | name   | description        |
+----+--------+--------------------+
|  1 | 技术   | 技术指导中心        |
|  2 | 市场   | 市场运营中心        |
|  3 | 财务   | 财务管理中心        |
+----+--------+--------------------+

#被关联中有数据后，向关联表中插入数据，保证了插入的“1”是被关联表中已存在的
insert into staff_info values(1,'alex','male',1);
mysql> select * from staff_info;
+------+------+------+--------+
| id   | name | sex  | dep_id |
+------+------+------+--------+
|    1 | alex | male |      1 |
+------+------+------+--------+

#如果没有事先创建被关联表和数据时，插入外键数据时会报错，因为“1”在被关联表中是不存在的
mysql> insert into staff_info values(1,'alex','male',1);
ERROR 1452 (23000): Cannot add or update a child row: a foreign key constraint fails (`db1`.`staff_info`, CONSTRAINT `staff_info_ibfk_1` FOREIGN KEY (`dep_id`) REFERENCES `department` (`id`) ON DELETE CASCADE ON UPDATE CASCADE)
```



**普通删除数据**

```mysql
#如果先删除正在引用的表数据，再删除被关联的列数据，否则会报错，因为其数据正被关联表所引用着
mysql> delete from department;
ERROR 1451 (23000): Cannot delete or update a parent row: a foreign key constraint fails (`db1`.`staff_info`, CONSTRAINT `staff_info_ibfk_1` FOREIGN KEY (`dep_id`) REFERENCES `department` (`id`))
```

所以，应该先删除关联表中的引用外键，再删除被关联表中的部门

```mysql
mysql> delete from staff_info where dep_id=1;

mysql> delete from department where id=1;
```



**级联删除数据**

```mysql
#on delete cascade表示级联删除， 美 /kæ'sked/串联
#on update cascade表示级联更新
create table staff_info(
	id int,
	name char(5),
	sex enum('male','female'),
	dep_id int,
	foreign key(dep_id) references department(id) on delete cascade on update cascade
);
```

这样再删除被关联表的部门数据时，员工表中的数据也会被级联修改和删除

```mysql
#首先查看表中的源数据
mysql> select * from staff_info;
+------+-------+------+--------+
| id   | name  | sex  | dep_id |
+------+-------+------+--------+
|    1 | alex  | male |      1 |
|    2 | peiqi | male |      2 |
|    3 | wxx   | male |      3 |
+------+-------+------+--------+

mysql> select * from department;
+----+--------+--------------------+
| id | name   | description        |
+----+--------+--------------------+
|  1 | 技术   | 技术研发中心        |
|  2 | 市场   | 市场运营中心        |
|  3 | 财务   | 财务管理中心        |
+----+--------+--------------------+

#删除被关联表中的数据，外键中关联的数据也被级联删除了
delete from department where id=1;

mysql> select * from staff_info;
+------+-------+------+--------+
| id   | name  | sex  | dep_id |
+------+-------+------+--------+
|    2 | peiqi | male |      2 |
|    3 | wxx   | male |      3 |
+------+-------+------+--------+
```



**级联更新数据**

```mysql
#被关联表数据更新后，关联表中也会级联更新
update department set id=4 where name='市场';

mysql> select * from staff_info;
+------+-------+------+--------+
| id   | name  | sex  | dep_id |
+------+-------+------+--------+
|    2 | peiqi | male |      4 |
|    3 | wxx   | male |      3 |
+------+-------+------+--------+

```



在实际的使用情况下，在逻辑角度尽量少的使用外键，因为会将表硬性的关联在一起
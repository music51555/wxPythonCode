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



建立部门表，部门表包含id、name，description字段，所以可以使用部门表的id字段作为员工表department列的外键，用id来区分员工隶属于哪个部门，所以部门表的一个部门相对于员工表的多个员工，使一对多的关系，所以部门表使主表，员工表使子表，在子表中添加外键

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



最终想要的简化结果，将员工表的某一列设置为外键，引用另一个表中的主键，达到表数据的完整性，减少冗余信息的显示

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

**1、先建立被主表（部门表），主表为备选表，从备选表中取值放入子表中**

**要保证主表的外键列，是唯一的，unique或是主键，且数据类型必须匹配**

```mysql
 #先创建被关联的部门表，因为在创建关联员工表的外键时，会references被关联表及其关联列，否则会提示表不存在
 create table department(
	id int primary key,
	name char(5),
	description char(20)
);
```



**2、再建立子表（员工表），从主表中取值，放入子表**

表示员工表的dep_id作为员工表的外键

```mysql
create table staff_info(
	id int,
	name char(5),
	sex enum('male','female'),
	dep_id int,
	foreign key(dep_id) references department(id)
);

mysql> desc student;
+-------+----------+------+-----+---------+-------+
| Field | Type     | Null | Key | Default | Extra |
+-------+----------+------+-----+---------+-------+
| id    | int(11)  | NO   | PRI | NULL    |       |
| name  | char(10) | YES  |     | NULL    |       |
| grade | int(11)  | YES  | MUL | NULL    |       |  #设置了外键的列，在key列添加了MUL标识
+-------+----------+------+-----+---------+-------+

```



**插入数据**

子表中的外键在插入数据时，要保障主表中已存在的对应的内容，所以先插入被主表中的数据

```mysql
#先插入主表的数据，保证了被主表中的数据是存在的
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

#被主表中有数据后，向子表表中插入数据，保证了插入的“1”在主表中是存在的
insert into staff_info values(1,'alex','male',1);
mysql> select * from staff_info;
+------+------+------+--------+
| id   | name | sex  | dep_id |
+------+------+------+--------+
|    1 | alex | male |      1 |
+------+------+------+--------+

#如果没有事先创建主表和数据时，插入外键数据时会报错，因为“1”在主表中是不存在的
mysql> insert into staff_info values(1,'alex','male',1);
ERROR 1452 (23000): Cannot add or update a child row: a foreign key constraint fails (`db1`.`staff_info`, CONSTRAINT `staff_info_ibfk_1` FOREIGN KEY (`dep_id`) REFERENCES `department` (`id`) ON DELETE CASCADE ON UPDATE CASCADE)
```



**普通删除数据**

```mysql
#如果先删除主表数据，再删除子表数据，会报错，因为主表数据正被子表所引用着
mysql> delete from department;
ERROR 1451 (23000): Cannot delete or update a parent row: a foreign key constraint fails (`db1`.`staff_info`, CONSTRAINT `staff_info_ibfk_1` FOREIGN KEY (`dep_id`) REFERENCES `department` (`id`))
```

所以，应该先删除子表中的引用外键，再删除主表中的部门

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

这样再删除被主表的部门数据时，子表中的数据也会被级联修改和删除

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

#删除主表中的数据，子表数据也被级联删除了
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
#主数据更新后，子表中也会级联更新
update department set id=4 where name='市场';

mysql> select * from staff_info;
+------+-------+------+--------+
| id   | name  | sex  | dep_id |
+------+-------+------+--------+
|    2 | peiqi | male |      4 |
|    3 | wxx   | male |      3 |
+------+-------+------+--------+

```



**删除外键**

```mysql
alter table teach2cls drop foreign key teach2cls_ibfk_2;
```





在实际的使用情况下，在逻辑角度尽量少的使用外键，因为会将表硬性的关联在一起
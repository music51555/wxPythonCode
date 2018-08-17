 #查询平均年龄大于30岁的部门名

```mysql
#分析，确定要连接的表，先形成笛卡尔积
mysql> select * from employee,department;
+----+------------+--------+------+--------+------+--------------+
| id | name       | sex    | age  | dep_id | id   | name         |
+----+------------+--------+------+--------+------+--------------+
|  1 | egon       | male   |   18 |    200 |  200 | 技术         |
|  1 | egon       | male   |   18 |    200 |  201 | 人力资源     |
|  1 | egon       | male   |   18 |    200 |  202 | 销售         |
|  1 | egon       | male   |   18 |    200 |  203 | 运营         |
|  2 | alex       | female |   48 |    201 |  200 | 技术         |
|  2 | alex       | female |   48 |    201 |  201 | 人力资源     |
|  2 | alex       | female |   48 |    201 |  202 | 销售         |
|  2 | alex       | female |   48 |    201 |  203 | 运营         |
|  3 | wupeiqi    | male   |   38 |    201 |  200 | 技术         |
|  3 | wupeiqi    | male   |   38 |    201 |  201 | 人力资源     |
|  3 | wupeiqi    | male   |   38 |    201 |  202 | 销售         |
|  3 | wupeiqi    | male   |   38 |    201 |  203 | 运营         |
|  4 | yuanhao    | female |   28 |    202 |  200 | 技术         |
|  4 | yuanhao    | female |   28 |    202 |  201 | 人力资源     |
|  4 | yuanhao    | female |   28 |    202 |  202 | 销售         |
|  4 | yuanhao    | female |   28 |    202 |  203 | 运营         |
|  5 | liwenzhou  | male   |   18 |    200 |  200 | 技术         |
|  5 | liwenzhou  | male   |   18 |    200 |  201 | 人力资源     |
|  5 | liwenzhou  | male   |   18 |    200 |  202 | 销售         |
|  5 | liwenzhou  | male   |   18 |    200 |  203 | 运营         |
|  6 | jingliyang | female |   18 |    204 |  200 | 技术         |
|  6 | jingliyang | female |   18 |    204 |  201 | 人力资源     |
|  6 | jingliyang | female |   18 |    204 |  202 | 销售         |
|  6 | jingliyang | female |   18 |    204 |  203 | 运营         |
+----+------------+--------+------+--------+------+--------------+

#添加on进行连表操作，找相等的对应关系，并选择连接方式，inner，left，right
mysql> select * from employee inner join department on employee.dep_id = department.id;
+----+-----------+--------+------+--------+------+--------------+
| id | name      | sex    | age  | dep_id | id   | name         |
+----+-----------+--------+------+--------+------+--------------+
|  1 | egon      | male   |   18 |    200 |  200 | 技术         |
|  2 | alex      | female |   48 |    201 |  201 | 人力资源     |
|  3 | wupeiqi   | male   |   38 |    201 |  201 | 人力资源     |
|  4 | yuanhao   | female |   28 |    202 |  202 | 销售         |
|  5 | liwenzhou | male   |   18 |    200 |  200 | 技术         |
+----+-----------+--------+------+--------+------+--------------+

#确定分组依据，题目说的查询结果是部门名，所以分组条件是部门
mysql> select department.name,avg(age) from employee inner join department on employee.dep_id = department.id group by department.name;
+--------------+----------+
| name         | avg(age) |
+--------------+----------+
| 人力资源     |  43.0000 |
| 技术         |  18.0000 |
| 销售         |  28.0000 |
+--------------+----------+


#添加having过滤，题目说平均年龄大于30岁
mysql> select department.name,avg(age) from employee inner join department on employee.dep_id = department.id group by department.name having avg(age)>30;
+--------------+----------+
| name         | avg(age) |
+--------------+----------+
| 人力资源     |  43.0000 |
+--------------+----------+


```



**select语法执行顺序**

1、先找到左右两张表，先形成笛卡尔积

2、添加on进行连表操作，找相等的对应关系，并选择连接方式，inner，left，right

3、有无where过滤

4、执行group by

5、having

6、select列表，还没有打印

7、去重

8、排序

9、限制显示条数
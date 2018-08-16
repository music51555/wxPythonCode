where，约束条件，不能使用聚合函数当条件

having，过滤，在分组之后过滤，可以使用聚合函数当条件

**习题**

```mysql
#查询各岗位内包含的员工个数小于2的岗位名、岗位内包含员工名字、个数
mysql> select post,group_concat(name),count(id) from employee group by post having count(id)<2;
+-----------------------------------------+--------------------+-----------+
| post                                    | group_concat(name) | count(id) |
+-----------------------------------------+--------------------+-----------+
| 老男孩驻沙河办事处外交大使                  | egon               |         1 |
+-----------------------------------------+--------------------+-----------+


#查询各岗位平均薪资大于10000的岗位名、平均工资
mysql> select post,avg(salary) from employee group by post having avg(salary)>10000;
+-----------+---------------+
| post      | avg(salary)   |
+-----------+---------------+
| operation |  16800.026000 |
| teacher   | 151842.901429 |
+-----------+---------------+

#查询各岗位平均薪资大于10000且小于20000的岗位名、平均工资
mysql> select post,avg(salary) from employee group by post having avg(salary)>10000 and avg(salary)<20000;
+-----------+--------------+
| post      | avg(salary)  |
+-----------+--------------+
| operation | 16800.026000 |
+-----------+--------------+
```




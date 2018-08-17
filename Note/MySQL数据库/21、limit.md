limit

限制显示条数

```mysql
mysql> select id,name,age from employee limit 3;
+----+---------+-----+
| id | name    | age |
+----+---------+-----+
|  1 | egon    |  18 |
|  2 | alex    |  78 |
|  3 | wupeiqi |  81 |
+----+---------+-----+
```



分页

```mysql
#描述从第几条取到第几条数据
mysql> select id,name,age from employee limit 0,5;
+----+-----------+-----+
| id | name      | age |
+----+-----------+-----+
|  1 | egon      |  18 |
|  2 | alex      |  78 |
|  3 | wupeiqi   |  81 |
|  4 | yuanhao   |  73 |
|  5 | liwenzhou |  28 |
+----+-----------+-----+


mysql> select id,name,age from employee limit 5,5;
+----+------------+-----+
| id | name       | age |
+----+------------+-----+
|  6 | jingliyang |  18 |
|  7 | jinxin     |  18 |
|  8 | 成龙       |  48 |
|  9 | 歪歪       |  48 |
| 10 | 丫丫       |  38 |
+----+------------+-----+

mysql> select id,name,age from employee limit 10,5;
+----+-----------+-----+
| id | name      | age |
+----+-----------+-----+
| 11 | 丁丁      |  18 |
| 12 | 星星      |  18 |
| 13 | 格格      |  28 |
| 14 | 张野      |  28 |
| 15 | 程咬金    |  18 |
+----+-----------+-----+

mysql> select id,name,age from employee limit 15,5;
+----+-----------+-----+
| id | name      | age |
+----+-----------+-----+
| 16 | 程咬银    |  18 |
| 17 | 程咬铜    |  18 |
| 18 | 程咬铁    |  18 |
+----+-----------+-----+
```


order by

默认升序，asc

```mysql
#无论是否加asc，默认都是升序，因为使用了order by排序
mysql> select name,age from employee order by age;
+------------+-----+
| name       | age |
+------------+-----+
| egon       |  18 |
| 程咬铜     |  18 |
| 程咬银     |  18 |
| 程咬金     |  18 |
| 星星       |  18 |
| 丁丁       |  18 |
| 程咬铁     |  18 |
| jinxin     |  18 |
| jingliyang |  18 |
| 格格       |  28 |
| 张野       |  28 |
| liwenzhou  |  28 |
| 丫丫       |  38 |

#降序，添加desc关键字
mysql> select name,age from employee order by age desc;
+------------+-----+
| name       | age |
+------------+-----+
| wupeiqi    |  81 |
| alex       |  78 |
| yuanhao    |  73 |
| 歪歪       |  48 |
| 成龙       |  48 |
| 丫丫       |  38 |
| 张野       |  28 |


#先按照age升序，如果age相同，则按照id降序排列
mysql> select id,name,age from employee order by age,id desc;
+----+------------+-----+
| id | name       | age |
+----+------------+-----+
| 18 | 程咬铁     |  18 |
| 17 | 程咬铜     |  18 |
| 16 | 程咬银     |  18 |
| 15 | 程咬金     |  18 |
| 12 | 星星       |  18 |
| 11 | 丁丁       |  18 |
|  7 | jinxin     |  18 |
|  6 | jingliyang |  18 |
|  1 | egon       |  18 |
| 14 | 张野       |  28 |
| 13 | 格格       |  28 |
|  5 | liwenzhou  |  28 |
| 10 | 丫丫       |  38 |
```
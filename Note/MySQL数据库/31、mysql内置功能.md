**视图**

把sql语句查询出的结果（虚拟表）保存下来，视图在硬盘中只有表结构文件，没有表数据文件

```mysql
#新增视图
#对多张表的查询结果，存储为视图，视图不允许被修改，虽然可以对单张表创建视图和修改视图，但是没有意义且不合理
create view teacher2course as select * from teacher inner join course on teacher.tid=course.teacher_id;

mysql> select * from teacher2course;
+-----+-----------------+-----+--------+------------+
| tid | tname           | cid | cname  | teacher_id |
+-----+-----------------+-----+--------+------------+
|   1 | 张磊老师        |   1 | 生物   |          1 |
|   2 | 李平老师        |   2 | 物理   |          2 |
|   2 | 李平老师        |   4 | 美术   |          2 |
|   3 | 刘海燕老师      |   3 | 体育   |          3 |
+-----+-----------------+-----+--------+------------+

#修改视图，也就是将sql语句更换
alter view teacher_view as select * from course where cid>3;

#删除视图
drop view teacher2course;
```

不建议使用，因为数据库的开发会更多的依赖于视图，数据库的结构和数据变化，视图也会随之而变化，且修改视图数据后，源表中的数据也会随之而被改变




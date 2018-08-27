43、查询不同课程但成绩相同的学生的学号、课程号、学生成绩；

```mysql
#思路：
#1、分别查询成绩表，并inner join合并为一张表，连接条件是每张表的成绩相同，学生id不同，课程id不同，这样就查找出成绩相同，但课程不同的学生信息
#2、在select...中分别列出每一张表的学生id、课程id和成绩
#3、在编写过程中遇到了误区，就是在其中一张表中出现了重复的学生信息，那是因为这一张表的成绩与另一张表不同课程的成绩相同，所以是正确的展示结果
mysql> select student_id,course_id,score,t2.t2_student_id,t2.t2_course_id,t2.t2_score from score as t1
    -> inner join
    -> (select student_id as t2_student_id,course_id as t2_course_id,score as t2_score from score) as t2
    -> on t1.score=t2.t2_score and t1.course_id!=t2.t2_course_id;
+------------+-----------+-------+---------------+--------------+----------+
| student_id | course_id | score | t2_student_id | t2_course_id | t2_score |
+------------+-----------+-------+---------------+--------------+----------+
|          1 |         4 |    22 |             4 |            1 |       22 |
|          2 |         3 |    15 |             7 |            5 |       15 |
|          2 |         5 |    50 |             4 |            2 |       50 |
|          2 |         5 |    50 |             7 |            9 |       50 |
|          7 |         5 |    15 |             2 |            3 |       15 |
|          7 |         4 |   100 |             1 |            9 |      100 |
|          7 |         4 |   100 |             4 |            9 |      100 |
|          5 |         5 |    55 |             7 |            2 |       55 |
|          6 |         5 |    10 |             2 |            4 |       10 |
|          1 |         9 |   100 |             7 |            4 |      100 |
|          4 |         1 |    22 |             1 |            4 |       22 |
|          4 |         2 |    50 |             2 |            5 |       50 |
|          4 |         2 |    50 |             7 |            9 |       50 |
|          4 |         9 |   100 |             7 |            4 |      100 |
|          7 |         9 |    50 |             2 |            5 |       50 |
|          7 |         9 |    50 |             4 |            2 |       50 |
|          7 |         2 |    55 |             5 |            5 |       55 |
|          2 |         4 |    10 |             6 |            5 |       10 |
+------------+-----------+-------+---------------+--------------+----------+
```



44、查询每门课程成绩最好的前两名学生id和姓名；

```mysql
#思路：
#1、在成绩表中按课程id查询出按成绩降序的前2条结果
#2、使用union连接两张表
#3、在使用union时，如果查询语句中包含order by必须添加括号（），但不用设置别名
#4、如果第一个查询语句使用了（），第二个查询语句也必须使用（）
mysql> (select student_id,course_id,score from score where course_id=1 order by score desc limit 2)
    -> union
    -> (select student_id,course_id,score from score where course_id=2 order by score desc limit 2)
    -> union
    -> (select student_id,course_id,score from score where course_id=3 order by score desc limit 2)
    -> union
    -> (select student_id,course_id,score from score where course_id=4 order by score desc limit 2)
    -> union
    -> (select student_id,course_id,score from score where course_id=5 order by score desc limit 2);
+------------+-----------+-------+
| student_id | course_id | score |
+------------+-----------+-------+
|          1 |         1 |    90 |
|          7 |         1 |    78 |
|          2 |         2 |    87 |
|          1 |         2 |    76 |
|          6 |         3 |    65 |
|          1 |         3 |    59 |
|          7 |         4 |   100 |
|          1 |         4 |    22 |
|          1 |         5 |    72 |
|          5 |         5 |    55 |
+------------+-----------+-------+
```



45、检索至少选修两门课程的学生学号；

```mysql
#思路：
#1、在成绩表中查询按学生id分组，使用count统计出每个学生报考的课程数>2的学生
mysql> select t1.sid from student as t1 inner join (select * from score group by student_id having count(course_id)>2) as t2 on t1.sid=t2.student_id;
+-----+
| sid |
+-----+
|   1 |
|   2 |
|   4 |
|   5 |
|   6 |
|   7 |
+-----+
```



46、查询没有学生选修的课程的课程号和课程名；

```mysql
#思路：
#1、在成绩表中查询出所有学生所选修的课程id
#2、在课程表中查询出所有的课程id
#3、查询所有的课程id中，有哪些not in步骤1的结果中，那么就是没有被选修的课程
mysql> select cid,cname from course as t1
    -> inner join
    -> (select cid as aa from course where cid not in (select distinct course_id from score)) as t2
    -> on t1.cid=t2.aa;
+-----+--------+
| cid | cname  |
+-----+--------+
|   7 | 地理   |
|   8 | 户外   |
+-----+--------+
```



47、查询没带过任何班级的老师id和姓名；

```mysql
#思路：
#1、在老师和班级的关系表，查询出所有老师的id
#2、在老师表中查询出所有的教师id，并查看这些id有哪些不在步骤1中的id结果中
mysql> select tid,tname from teacher where tid not in  (select distinct tid from teach2cls);
+-----+--------+
| tid | tname  |
+-----+--------+
|   6 | 李虹   |
+-----+--------+
```



48、查询有两门以上课程超过80分的学生id及其平均成绩；

```mysql
#思路：
#1、在成绩表中查询按学生id分组，添加where条件，过滤出成绩>80的学生，且统计出课程数>2
#2、在成绩表中按学生id分组，查询出每个学生的平均成绩
#3、在步骤2添加where条件，等于步骤1中的学生id，连接两张表，查询出结果
mysql> select student_id,avg(score) from score where student_id=(select student_id from score where score>80 group by student_id having count(course_id)>2) group by student_id; 
+------------+------------+
| student_id | avg(score) |
+------------+------------+
|          1 |    73.8571 |
+------------+------------+
```



49、检索“3”课程分数小于60，按分数降序排列的同学学号；

```mysql
#思路：
#1、在成绩表中查询出课程id为3的所有信息
#2、添加where条件，成绩<60分
#3、降序排列成绩，输出信息
mysql> select * from score where course_id=3 and score<60 order by score desc;
+-----+------------+-----------+-------+
| sid | student_id | course_id | score |
+-----+------------+-----------+-------+
|   6 |          1 |         3 |    59 |
|  47 |          7 |         3 |    56 |
|   4 |          2 |         3 |    15 |
+-----+------------+-----------+-------+
```



50、删除编号为“2”的同学的“1”课程的成绩；

```mysql
#思路：
#1、在成绩表中删除数据
#2、添加条件学号=2，课程id=1
mysql> delete from score where course_id=1 and student_id=2;
Query OK, 1 row affected (0.03 sec)
```



51、查询同时选修了物理课和生物课的学生id和姓名；

```mysql
#思路：
#1、先在成绩表中查询出报考了生物课程的学生
#2、再在成绩表中查询出报考了物理课程的学生
#3、使用inner join连接2张表，查询出同时选了这2门课程的学生id
#4、连接学生表查询出姓名
mysql> select sid,sname from student as t3
    -> inner join
    -> (select t1.student_id from score as t1
    -> inner join
    -> (select student_id from score where course_id=(select cid from course where cname='生物')) as t2
    -> on t1.student_id=t2.student_id
    -> where course_id=(select cid from course where cname='物理')) as t4
    -> on t3.sid=t4.student_id
    -> ;
+-----+--------+
| sid | sname  |
+-----+--------+
|   1 | 乔丹   |
|   7 | 乔里   |
+-----+--------+
```


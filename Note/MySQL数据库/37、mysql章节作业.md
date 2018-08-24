1、自行创建测试数据；

```mysql
#思路：
#1、根据给的表结构创建表和数据
#2、在完成sql题目的过程中补充数据
mysql> show tables;
+--------------+
| Tables_in_m4 |
+--------------+
| class        |
| class_grade  |
| course       |
| score        |
| student      |
| teach2cls    |
| teacher      |
+--------------+
```



2、查询学生总人数；

```mysql
#思路：
#1、在学生表中使用聚合函数count统计学生人数
mysql> select count(*) as total_student from student;
+---------------+
| total_student |
+---------------+
|             3 |
+---------------+
```



3、查询“生物”课程和“物理”课程成绩都及格的学生id和姓名；

```mysql
#思路：
#1、在课程表中查询出生物和物理课程的课程id
#2、在成绩表中查询成绩及格，且课程id的在生物和物理课程的id范围内（in）
#3、连接学生表，查询出姓名姓名和学号
mysql> select t1.sid,sname from student as t1 inner join (select * from score where score>60 and course_id in (select cid from course where cname in ('生物',' 物理'))) as t2 on t1.sid=t2.student_id;
+-----+--------+
| sid | sname  |
+-----+--------+
|   3 | 科比   |
|   7 | 库里   |
+-----+--------+
```



4、查询每个年级的班级数，取出班级数最多的前三个年级；

```mysql
#思路：
#1、在班级表中按年级分组，统计每个年级的班级数
#2、降序排序
#3、limit取前三名
mysql> select count(*) as total_class from class group by grade_id order by total_class desc limit 3;
+-------------+
| total_class |
+-------------+
|           2 |
|           1 |
|           1 |
+-------------+
```



5、查询平均成绩最高和最低的学生的id和姓名以及平均成绩；

```mysql
#思路：
#在成绩表中按学生分组，查询出每个学生的平均成绩，并降序排列，取第一个
#再次升序排列，取第一个
#连接平均成绩最高和最低的2张表
#再连接学生表，查询出学生的姓名
mysql> select t1.sname,t2.student_id from student as t1 inner join ((select student_id,avg(score) as avg_score from score group by student_id order by avg_score desc limit 1) union (select student_id,avg(score) as avg_score from score group by student_id order by avg_score asc limit 1)) as t2 on t1.sid=t2.student_id;
+--------+------------+
| sname  | student_id |
+--------+------------+
| 科比   |          3 |
| 乔丹   |          1 |
+--------+------------+
```



6、查询每个年级的学生人数；

```mysql
#思路：
#1、在班级表中按年级id分组，查询出每个年级的班级数和班级id
#2、连接学生表和班级id匹配，查询学生的总数
mysql> select class.caption,count(student.sid) as total_student from class inner join student on class.cid=student.class_id group by class.grade_id;
+--------------+---------------+
| caption      | total_student |
+--------------+---------------+
| 一年一班     |             2 |
| 二年一班     |             2 |
| 三年一班     |             2 |
| 四年一班     |             1 |
+--------------+---------------+
```



7、查询每位学生的学号，姓名，选课数，平均成绩；

```mysql
#思路：
#1、先在成绩表中按学生id分组，查询出每位学生的平均成绩和选课总数
#2、连接学生表查询学生的姓名
mysql> select t1.sid,t1.sname,t2.course_count,t2.avg_score from student as t1 inner join (select student_id,count(sid) as course_count,avg(score) as avg_score from score group by student_id) as t2 on t1.sid=t2.student_id;
+-----+-----------+--------------+-----------+
| sid | sname     | course_count | avg_score |
+-----+-----------+--------------+-----------+
|   1 | 乔丹      |            5 |   54.4000 |
|   2 | 艾佛森    |            5 |   60.8000 |
|   3 | 科比      |            1 |  100.0000 |
|   4 | 奥尼尔    |            1 |   96.0000 |
|   5 | 麦迪      |            2 |   66.0000 |
|   6 | 詹姆斯    |            2 |   75.0000 |
|   7 | 库里      |            3 |   67.6667 |
+-----+-----------+--------------+-----------+
```



8、查询学生编号为“2”的学生的姓名、该学生成绩最高的课程名、成绩最低的课程名及分数；

```mysql
#思路：
#1、在成绩表中查询学号为2的学生的最高成绩
#2、在成绩表中查询学号为2的学生的最低成绩
#3、全外连接2张表，合并为学号为2的学生的最高成绩和最低成绩表
#4、连接课程表查询课程名称
#5、连接学生表查询学生姓名
mysql> select t3.sname,t4.cname,t4.score from student as t3 inner join (select * from course as t1 inner join (select student_id,course_id,score from score where score in (select min(score) from score where student_id=2) and student_id=2 union select student_id,course_id,score from score where score in (select max(score) from score where student_id=2) and student_id=2) as t2 on t1.cid=t2.course_id) as t4 on t3.sid=t4.student_id;
+-----------+--------+-------+
| sname     | cname  | score |
+-----------+--------+-------+
| 艾佛森    | 体育   |    99  |
| 艾佛森    | 物理   |    15  |
+-----------+--------+-------+
```



9、查询姓“李”的老师的个数和所带班级数；

```mysql
#思路：
#1、先在老师表中查询姓李老师的个数
#2、连接老师和班级的关系表teach2cls，统计出老师所带的班级个数
mysql> select t2.teacher_li_count,count(t1.cid) as count_course from teach2cls as t1 inner join (select tid,count(tid) as teacher_li_count from teacher where tname like '李%') as t2 on t1.tid=t2.tid;
+------------------+--------------+
| teacher_li_count | count_course |
+------------------+--------------+
|                2 |            2 |
+------------------+--------------+
```



10、查询班级数小于5的年级id和年级名；

```mysql
#思路：
#1、先在班级表中，按年级分组，统计每个年级班级的数量
#2、添加having过滤，查询班级数小于5的年级
#3、连接年级表，查看年级id和年级名
mysql> select t1.gid,t1.gname from class_grade as t1 inner join (select grade_id,count(caption) from class group by grade_id having count(caption)<5) as t2 on t1.gid=t2.grade_id;
+-----+-----------+
| gid | gname     |
+-----+-----------+
|   2 | 二年级    |
|   4 | 四年级    |
+-----+-----------+
```



11、查询班级信息，包括班级id、班级名称、年级、年级级别(12为低年级，34为中年级，56为高年级)，示例结果如下；

| 班级id | 班级名称 | 年级   | 年级级别 |
| ------ | -------- | ------ | -------- |
| 1      | 一年一班 | 一年级 | 低       |

```mysql
#思路
#通过case when ... then ... end流程控制语法设置展示的结果
#case when t2.gid in (1,2) then '低年级' end
#列名通过as '班级id'，as '班级名称'来实现
mysql> select t1.cid as '班级id',t1.caption as '班级名称',t2.gname as '年级',(case when t2.gid in (1,2) then '低年级' when t2.gid in (3,4) then '中年级' when t2.gid in (5,6) then '高年级' end) as '年级级别' from class as t1 inner join class_grade as t2 on t1.grade_id=t2.gid;
+----------+--------------+-----------+--------------+
| 班级id   | 班级名称     | 年级      | 年级级别     |
+----------+--------------+-----------+--------------+
|        1 | 一年一班     | 一年级    | 低年级       |
|        8 | 一年二班     | 一年级    | 低年级       |
|        9 | 一年三班     | 一年级    | 低年级       |
|       10 | 一年四班     | 一年级    | 低年级       |
|       15 | 一年五班     | 一年级    | 低年级       |
|       16 | 一年六班     | 一年级    | 低年级       |
|        2 | 二年一班     | 二年级    | 低年级       |
|       11 | 二年二班     | 二年级    | 低年级       |
|       12 | 二年三班     | 二年级    | 低年级       |
|        3 | 三年一班     | 三年级    | 中年级       |
|        4 | 三年二班     | 三年级    | 中年级       |
|       13 | 三年三班     | 三年级    | 中年级       |
|       14 | 三年四班     | 三年级    | 中年级       |
|       17 | 三年五班     | 三年级    | 中年级       |
|        5 | 四年一班     | 四年级    | 中年级       |
|       18 | 四年二班     | 四年级    | 中年级       |
|       19 | 四年三班     | 四年级    | 中年级       |
|       20 | 五年一班     | 五年级    | 高年级       |
|       21 | 五年二班     | 五年级    | 高年级       |
|       22 | 五年三班     | 五年级    | 高年级       |
|       23 | 五年四班     | 五年级    | 高年级       |
+----------+--------------+-----------+--------------+
```



12、查询学过“张三”老师2门课以上的同学的学号、姓名；

```mysql
#思路：
#1、首先查询出张三老师的teach_id
#2、在课程表中查询出张三老师所教的所有程程id
#3、在成绩表中根据张三老师课程的所有course_id，查询有哪些学生报名，并使用聚合函数过滤count(course_id)>2
#4、连接学生表，查询学生的姓名
mysql> select t1.sname,t2.student_id from student as t1 inner join ( select student_id from score where course_id in (select cid from course where teacher_id = (select tid from teacher where tid=1)) group by student_id having count(course_id)>2) as t2 on t1.sid=t2.student_id;
+--------+------------+
| sname  | student_id |
+--------+------------+
| 乔丹   |          1 |
+--------+------------+
1 row in set (0.00 sec)
```



13、查询教授课程超过2门的老师的id和姓名；

```mysql
#思路：
#在课程表中按teacher_id分组，并having过滤出课程总数大于2的课程
#连接老师表，查询出出老师姓名
mysql> select t1.tname,t2.teacher_id from teacher as t1 inner join (select teacher_id from course group by teacher_id having count(cid) > 2) as t2 on t1.tid=t2.teacher_id;
+--------+------------+
| tname  | teacher_id |
+--------+------------+
| 张三   |          1 |
+--------+------------+
1 row in set (0.00 sec)
```



14、查询学过编号“1”课程和编号“2”课程的同学的学号、姓名；

```mysql
#思路：
#1、先在课程表中查询出课程编号为1和2的课程id
#2、根据查询结果，在课成绩表中查询报考了这些课程的所有学生id
#3、连接学生表，查询出学生id和学生姓名
mysql> select sid,sname from student as t1 inner join (select distinct student_id from score where course_id in (select cid from course where cid=1 or cid=2)) as t2 on t1.sid=t2.student_id;
+-----+-----------+
| sid | sname     |
+-----+-----------+
|   1 | 乔丹      |
|   2 | 艾佛森    |
|   3 | 科比      |
|   4 | 奥尼尔    |
|   5 | 麦迪      |
|   6 | 詹姆斯    |
|   7 | 库里      |
+-----+-----------+
```



15、查询没有带过高年级的老师id和姓名；

```mysql
#思路
#1、先在班级表中查询出高年级的班级id
#2、在teach2cls表中，查询出有哪些老师不教这些高年级的班，查询出老师id
#3、在老师表中查询出有哪些老师不在这些老师id中的，那么就是没有教过高年级的老师id
mysql> select * from teacher where tid not in (select distinct tid from teach2cls where cid in (select cid from class where grade_id>4));
+-----+--------+
| tid | tname  |
+-----+--------+
|   1 | 张三   |
|   5 | 李军   |
+-----+--------+
```



16、查询学过“张三”老师所教的所有课的同学的学号、姓名；

```mysql
#思路：
#1、首先在老师表查询出姓名为张三的老师id
#2、在课程表中按张三id查询出张三所教的所有课程
#3、在成绩表中按学生id分组，查询出每位学生报考张三课程的总数，设置为表t1
#4、再次查询老师表，查询出张三课程的总数，设置为表t2
#5、连接t1和t2表，查询出谁报考了所有张三的课程
#6、连接学生表，查询出学生姓名
mysql> select sid,sname from student as t1 inner join (select student_id from score where course_id in (select cid from course where teacher_id = (select tid from teacher where tname='张三')) group by student_id having count(course_id)=(select count(cid) from course where teacher_id = (select tid from teacher where tname='张三'))) as t2 on t1.sid=t2.student_id;
+-----+--------+
| sid | sname  |
+-----+--------+
|   1 | 乔丹   |
+-----+--------+
```



17、查询带过超过2个班级的老师的id和姓名；

```mysql
#思路：
#1、在老师和班级的关系表中按老师id分组，查询出每位老师带的班级数
#2、添加过滤条件，班级数>2的班级
#3、连接老师表，查询老师姓名
mysql> select t1.tid,t1.tname from teacher as t1 inner join (select tid,count(cid) as count_class from teach2cls group by tid having count_class>2) as t2 on t1.tid=t2.tid;
+-----+--------+
| tid | tname  |
+-----+--------+
|   1 | 张三   |
|   2 | 李四   |
|   3 | 王五   |
|   4 | 乔六   |
+-----+--------+
```



18、查询课程编号“2”的成绩比课程编号“1”课程低的所有同学的学号、姓名；

```mysql
#思路：
#1、在成绩表中查询出报考了课程2的所有学生，命名为t1
#2、再查询出报考了课程1的所有学生，命名为t2
#3、连接2张表，连接条件式学生id相同，因为要筛选出所有同时报考了课程1和课程2的学生
#4、添加where条件，t1的成绩>t2的成绩
#5、连接学生表查询姓名
mysql> select sid,sname from student as t1 inner join (select t1.student_id from score as t1 inner join (select * from score where course_id=1) as t2 on t1.student_id=t2.student_id where t1.course_id=2 and t1.score>t2.score) as t2 on t1.sid=t2.student_id;
+-----+-----------+
| sid | sname     |
+-----+-----------+
|   2 | 艾佛森    |
|   6 | 詹姆斯    |
+-----+-----------+
```



19、查询所带班级数最多的老师id和姓名；

```mysql
#思路：
#1、在老师班级的关系表中按老师分组，查看每个老师所带的班级总数
#2、降序排序后，取第一条
#3、连接老师表查询老师姓名
mysql> select t1.tid,t1.tname from teacher as t1 inner join (select tid,count(cid) from teach2cls group by tid order by count(cid) desc limit 1) as t2 on t1.tid=t2.tid;
+-----+--------+
| tid | tname  |
+-----+--------+
|   3 | 王五   |
+-----+--------+
```



20、查询有课程成绩小于60分的同学的学号、姓名；

```mysql
#思路：
#1、在成绩表中查询有不及格成绩的学生id，意思也就是这些同学有不及格的成绩
#2、连接学生表，查看学生姓名
select sid,sname from student as t1 inner join
(select distinct student_id from score where score<60) as t2
on t1.sid=t2.student_id;
+-----+-----------+
| sid | sname     |
+-----+-----------+
|   1 | 乔丹      |
|   2 | 艾佛森    |
|   3 | 科比      |
|   5 | 麦迪      |
|   6 | 詹姆斯    |
|   7 | 库里      |
+-----+-----------+
```



21、查询没有学全所有课的同学的学号、姓名；

```mysql
#思路：
#1、先在成绩表中查询出每位学生报考的课程总数
#2、再在课程表中查询出所有的课程总数
#3、添加过滤如果每位学生的课程总数不等于所有的课程总数，那么就是没选所有课的学生
select sid,sname from student as t1 inner join
(select student_id from score group by student_id having 
count(course_id) != (select count(cid) from course)) as t2
on t1.sid=t2.student_id;
```



22、查询至少有一门课与学号为“1”的同学所学相同的同学的学号和姓名；

```mysql
#思路：
#1、在成绩表中查询出学号为1的学生报考了哪些课程
#2、继续在成绩表中查询出哪些学号不是1的学生，报考的课程id在步骤1的结果中
mysql> select distinct sid,sname from student as t1 inner join (select student_id from score where course_id in (select course_id from score where student_id=1) and student_id!=1) as t2 on t1.sid=t2.student_id;
+-----+-----------+
| sid | sname     |
+-----+-----------+
|   2 | 艾佛森    |
|   3 | 科比      |
|   4 | 奥尼尔    |
|   5 | 麦迪      |
|   6 | 詹姆斯    |
|   7 | 库里      |
+-----+-----------+
```



23、查询至少学过学号为“1”同学所选课程中任意一门课的**其他同学**学号和姓名；

```
与导师沟通，与上一题重复
```



24、查询和“2”号同学学习的课程完全相同的其他同学的学号和姓名；

```mysql
#思路：
#1、首先成绩表中查询出2号学生所学的课程总数
#2、再在成绩表中查询出和2号学生所学课程总数相等的学生
#3、再添加过滤，不仅和2好学生所学课程总数一致，且课程总数相加的和也相等，那么就可以确定这名学生和2号学生报名了相同的课程
mysql> select sid,sname from student as t1 inner join (select student_id from score group by student_id having count(course_id)=(select count(course_id) from score where student_id=2) and sum(course_id)=(select sum(course_id) from score where student_id=2)) as t2 on t1.sid=t2.student_id;
+-----+-----------+
| sid | sname     |
+-----+-----------+
|   2 | 艾佛森    |
|   6 | 詹姆斯    |
+-----+-----------+
```



25、删除学习“张三”老师课的score表记录；

```mysql
#思路：
#1、首先在老师表中查询出张三老师的教师id
#2、在课程表中查询出张三老师所教课程的课程id
#3、在成绩表中删除课程id为张三老师的课程id的成绩记录
mysql> delete from score where course_id in (select cid from course where teacher_id=(select tid from teacher where tname='张三'));
Query OK, 14 rows affected (0.04 sec)
```



26、向score表中插入一些记录，这些记录要求符合以下条件：①没有上过编号“2”课程的同学学号；②插入“2”号课程的平均成绩；

```mysql
#思路：
#重点是向表中同时插入多条记录
#首先在成绩表中查询出上过课程2的学生
#继续在成绩表中通过not in查询出没有上过课程2的学生
#汇总查询结果，通过插入查询结果的方式插入数据，列的类型要匹配正确
insert into score(student_id,course_id,score)
	(select * from
	(select distinct student_id from score where student_id not in (select student_id from score where course_id=2)) as t1,
	(select distinct course_id from score where course_id=2) as t2,
	(select avg(score) from score where course_id=2) as t3)
```



27、按平均成绩从低到高显示所有学生的“语文”、“数学”、“英语”三门的课程成绩，按如下形式显示： 学生ID,语文,数学,英语,课程数,平均分；

```
#由原题的“语文”、“数学”、“英语”改为“体育”，“物理”，“化学”

```



28、查询各科成绩最高和最低的分：以如下形式显示：课程ID，最高分，最低分；

29、按各科平均成绩从低到高和及格率的百分数从高到低顺序；

30、课程平均分从高到低显示（现实任课老师）；

31、查询各科成绩前三名的记录(不考虑成绩并列情况)

32、查询每门课程被选修的学生数；

33、查询选修了2门以上课程的全部学生的学号和姓名；

34、查询男生、女生的人数，按倒序排列；

35、查询姓“张”的学生名单；

36、查询同名同姓学生名单，并统计同名人数；

37、查询每门课程的平均成绩，结果按平均成绩升序排列，平均成绩相同时，按课程号降序排列；

38、查询课程名称为“数学”，且分数低于60的学生姓名和分数；

39、查询课程编号为“3”且课程成绩在80分以上的学生的学号和姓名；

40、求选修了课程的学生人数

41、查询选修“王五”老师所授课程的学生中，成绩最高和最低的学生姓名及其成绩；

42、查询各个课程及相应的选修人数；

43、查询不同课程但成绩相同的学生的学号、课程号、学生成绩；

44、查询每门课程成绩最好的前两名学生id和姓名；

45、检索至少选修两门课程的学生学号；

46、查询没有学生选修的课程的课程号和课程名；

47、查询没带过任何班级的老师id和姓名；

48、查询有两门以上课程超过80分的学生id及其平均成绩；

49、检索“3”课程分数小于60，按分数降序排列的同学学号；

50、删除编号为“2”的同学的“1”课程的成绩；

51、查询同时选修了物理课和生物课的学生id和姓名；
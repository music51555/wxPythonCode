

选课系统开发，要求有四种角色:学校、学员、课程、讲师

**详细要求:**

1. 创建北京、上海 2 所学校

   程序设计：开放接口，由用户手动创建学校

2. 创建linux , python , go 3个课程 ， linux\py 在北京开， go 在上海开

3. 课程包含，周期，价格，通过学校创建课程

4. 通过学校创建班级， 班级关联课程、讲师（将创建的班级对象传入到课程和讲师类中，所以可以在上课时选择班级进行一系列操作，或了解老师所教的课程，如linux，python，可以通过课程查询出班级）

5. 创建学员时，选择学校，关联班级（将学生对象传入到班级类中，可以通过班级查看到有哪些同学）

6. **创建讲师角色时要关联学校**（将讲师对象传入到学校类中，可以了解到学校有哪些老师）

7. 提供两个角色接口

8. 为学员、讲师、管理员分别提供用户界面，并提供对应功能：

   1 学员视图， 可以注册， 交学费， 选择班级

   2 讲师视图， 讲师可管理自己的班级， 上课时选择班级， 查看班级学员列表 ， 修改所管理的学员的成绩 

   3 管理视图， 创建讲师， 创建班级，创建课程

*注1：上面的操作产生的数据都通过pickle序列化保存到文件里* 注2：此作业必须画流程图，图中标注好不同类或对象之间的调用关系
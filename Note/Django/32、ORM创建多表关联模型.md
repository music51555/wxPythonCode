ORM创建多表关联模型

##### 1、表的名称是app01_book

##### 2、如果没有写nid字段，Django会自动添加主键

##### 3、外键字段会被自动添加_idb

##### 4、在INSTALLED_APP添加应用名称

##### 5、null=True表示允许为空



#### 书籍表（与出版社表一对多关系，生成外键列_id）

#### （与作者表多对多关系，生成第三张关系表）

```python
class Book(models.Model):
    nid=models.AutoField(primary_key=True)
    title=models.CharField(max_length=20)
    publishDate=models.DateField()
    price=models.DecimalField(max_digits=5,decimal_places=2)
    # 一本书对应多个出版社，不；一个出版社对应多本书，是的。所以是一对多的关系，在多的表中创建关联列publish_id
    # 添加外键时不要加_id，Django会为其自动添加_id，该条语句在创建publish_id列的同时，又与Publish表创建了外键约束
    publish=models.ForeignKey(to="Publish",to_field='nid')

    # 一本书对应多个作者，同时一个作者也对应多本书，所以是多对多的关系，需要创建第三张关系表，使用当前表的主键，与另外一张表的主键，作为外键合并为一张新的关系表
    authors=models.ManyToManyField(to='Author')
   
    # 执行该行代码时，实则是执行了创建表类
    # class Book2Author(models.Model):
    #     nid = models.AutoField(primary_key=True)
    #     book = models.ForeignKey(to="Author", to_field="nid")
    #     author = models.ForeignKey(to="Book", to_field='nid')
    
    # 也是执行了创建表的sql语句
    # create book2author(
    #     nid int,
    #     book_id int,
    #     author_id int,
    #     foreign key book_id references book(nid),
    #     foreign key author_id rederences author(nid)
	# )
```
```python
#书籍表
mysql> desc app01_book;
+-------------+--------------+------+-----+---------+----------------+
| Field       | Type         | Null | Key | Default | Extra          |
+-------------+--------------+------+-----+---------+----------------+
| nid         | int(11)      | NO   | PRI | NULL    | auto_increment |
| title       | varchar(20)  | NO   |     | NULL    |                |
| publishDate | date         | NO   |     | NULL    |                |
| price       | decimal(5,2) | NO   |     | NULL    |                |
| publish_id  | int(11)      | NO   | MUL | NULL    |                |
+-------------+--------------+------+-----+---------+----------------+
5 rows in set (0.00 sec)
```

```mysql
# 多对多关系，书籍和作者的关系表，MUL外键
mysql> desc app01_book_authors;
+-----------+---------+------+-----+---------+----------------+
| Field     | Type    | Null | Key | Default | Extra          |
+-----------+---------+------+-----+---------+----------------+
| id        | int(11) | NO   | PRI | NULL    | auto_increment |
| book_id   | int(11) | NO   | MUL | NULL    |                |
| author_id | int(11) | NO   | MUL | NULL    |                |
+-----------+---------+------+-----+---------+----------------+
3 rows in set (0.00 sec)
```



#### 出版社表

```python
class Publish(models.Model):
    nid=models.AutoField(primary_key=True)
    name=models.CharField(max_length=25)
    city=models.CharField(max_length=15)
    email=models.EmailField()
```

```mysql
mysql> desc app01_publish;
+-------+--------------+------+-----+---------+----------------+
| Field | Type         | Null | Key | Default | Extra          |
+-------+--------------+------+-----+---------+----------------+
| nid   | int(11)      | NO   | PRI | NULL    | auto_increment |
| name  | varchar(25)  | NO   |     | NULL    |                |
| city  | varchar(15)  | NO   |     | NULL    |                |
| email | varchar(254) | NO   |     | NULL    |                |
+-------+--------------+------+-----+---------+----------------+
4 rows in set (0.00 sec)
```



#### 作者表（与作者详情表一对一关系，生成外键列_id）

```python
class Author(models.Model):
    nid=models.AutoField(primary_key=True)
    name=models.CharField(max_length=5)
    age=models.IntegerField()
    # 一对一的关系表中，在哪张表中建立外键都可以，在作者表中建立外键指向作者详情表中的某一条数据更习惯，外键作者表的nid，一个作者对应一条作者的细信息
    # to="AuthorDetail"也可以写为to=AuthorDetail，不添加双引号，但可能由于代码执行顺序问题，找不到表类名AuthorDetail
    # 对比于ForeignKey方法，因为是一对一的关系，一个作者只对应自己的一条个人信息，有唯一约束，所以外键列会有unique唯一约束
    authordetail=models.OneToOneField(to="AuthorDetail",to_field="nid")
```

```mysql
mysql> desc app01_author;
+-----------------+------------+------+-----+---------+----------------+
| Field           | Type       | Null | Key | Default | Extra          |
+-----------------+------------+------+-----+---------+----------------+
| nid             | int(11)    | NO   | PRI | NULL    | auto_increment |
| name            | varchar(5) | NO   |     | NULL    |                |
| age             | int(11)    | NO   |     | NULL    |                |
| authordetail_id | int(11)    | NO   | UNI | NULL    |                |
+-----------------+------------+------+-----+---------+----------------+
4 rows in set (0.00 sec)
```



#### 作者详情表

```python
class AuthorDetail(models.Model):
    nid=models.AutoField(primary_key=True)
    birthday=models.DateField()
    telephone=models.CharField(max_length=11)
    addr=models.CharField(max_length=30)
```

```mysql
mysql> desc app01_authordetail;
+-----------+-------------+------+-----+---------+----------------+
| Field     | Type        | Null | Key | Default | Extra          |
+-----------+-------------+------+-----+---------+----------------+
| nid       | int(11)     | NO   | PRI | NULL    | auto_increment |
| birthday  | date        | NO   |     | NULL    |                |
| telephone | varchar(11) | NO   |     | NULL    |                |
| addr      | varchar(30) | NO   |     | NULL    |                |
+-----------+-------------+------+-----+---------+----------------+
4 rows in set (0.00 sec)
```


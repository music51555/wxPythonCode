from django.db import models

class Book(models.Model):
    nid=models.AutoField(primary_key=True)
    title=models.CharField(max_length=20)
    publishDate=models.DateField()
    price=models.DecimalField(max_digits=5,decimal_places=2)
    # 一本书对应多个出版社，不；一个出版社对应多本书，是的。所以是一对多的关系，在多的表中创建关联列
    # 添加外键时不要加_id，Django会为其自动添加_id，该条语句在创建publish_id的同时，又与Publish表创建了外键约束
    # 如果没有写to_field，那么就是直接对应表的主键
    publish=models.ForeignKey(to="Publish",to_field='nid',on_delete=models.CASCADE)

    # 一本书对应多个作者，同时一个作者也对应多本书，所以是多对对的关系，需要创建第三章关系表
    authors=models.ManyToManyField(to='Author')
    # 执行该行代码时，实则是执行了创建表类
    # class Book2Author(models.Model):
    #     nid = models.AutoField(primary_key=True)
    #     book = models.ForeignKey(to="Author", to_field="nid")
    #     author = models.ForeignKey(to="Book", to_field='nid')

class Publish(models.Model):
    nid=models.AutoField(primary_key=True)
    name=models.CharField(max_length=25)
    city=models.CharField(max_length=15)
    email=models.EmailField()

class Author(models.Model):
    nid=models.AutoField(primary_key=True)
    name=models.CharField(max_length=5)
    age=models.IntegerField()
    # 一对一的关系表中，在哪张表中建立外键都可以，在作者表中建立外键指向作者详情表中的某一条数据更习惯，外键作者表的nid，一个作者对应一条作者的细信息
    # to="AuthorDetail"也可以写为to=AuthorDetail，不添加双引号，但可能由于代码执行顺序问题，找不到表类名
    # 对比于ForeignKey方法，有唯一约束
    authordetail=models.OneToOneField(to="AuthorDetail",to_field="nid",on_delete=models.CASCADE)

class AuthorDetail(models.Model):
    nid=models.AutoField(primary_key=True)
    birthday=models.DateField()
    telephone=models.CharField(max_length=11)
    addr=models.CharField(max_length=30)
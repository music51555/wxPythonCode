from django.db import models
from django.contrib.auth.models import AbstractUser

# 用户信息表。继承的AbstractUser类，本身就已经包含了username、password、email等字段，再额外的添加一些自定义的字段，实现自定义用户表，作为用户的接口表
class UserInfo(AbstractUser):
    nid=models.CharField(primary_key=True)
    telephone=models.CharField(max_length=11,null=True,unique=True)
    avatar=models.FileField(upload_to='avatars/',default='/avatars/default.png')
    # verbose_name指明一个易于理解和表述的对象名称, /vɝ'bos/  冗长的；啰嗦的
    create_time=models.DateTimeField(verbose_name='创建时间',auto_now_add=True)
    # 与Blog表是一对一的关系，一对一关系在哪张表中建立关系都是可以的，看更倾向于通过哪张表作为源头去查找
    blog=models.OneToOneField(to='Blog',to_field='nid',null=True)

    def __str__(self):
        return self.username

class Blog(models.Model):
    # 博客信息表也是站点表，一个用户对应一个博客，这三个属性也可以放在用户表中，但是为了解耦，可以单独存放
    nid=models.CharField(primary_key=True)
    title=models.CharField(verbose_name='个人博客标题',max_length=64)
    site_name=models.CharField(verbose_name='站点名称',max_length=64)
    theme=models.CharField(verbose_name='博客主题',max_length=32)

    def __str__(self):
        return self.title

class Category(models.Model):
    # 文章分类表
    # 一个用户对应一个站点，因为一个用户对应多个分类，所以一个站点也是对应多个分类
    nid=models.AutoField(primary_key=True)
    title=models.CharField(verbose_name='分类标题',max_length=32)
    # 根据用户表去查找站点表和分类表的关系，一个用户对应多个分类，用户和站点是一对一的关系，所以要创建站点和分类的关系也是一对多关系，在多的表中创建外键
    blog=models.ForeignKey(verbose_name='所属博客',to='Blog',to_field='nid')

    def __str__(self):
        return self.title

class Tag(models.Model):
    nid=models.AutoField(primary_key=True)
    title=models.CharField(verbose_name='标签名称',max_length=32)
    blog=models.ForeignKey(verbose_name='所属博客',to='Blog',to_field='nid')

    def __str__(self):
        return self.title

class Article(models.Model):
    # 基础字段
    nid=models.AutoField(primary_key=True)
    title=models.CharField(verbose_name='文章标题',max_length=50)
    desc=models.CharField(verbose_name='文章描述',max_length=255)
    create_time=models.DateTimeField(verbose_name='创建时间',auto_now_add=True)
    content=models.TextField()

    # 与用户的关系，一个用户对应多篇文章，一篇文章对应一个用户，多对多关系在多的表中创建关系
    user=models.ForeignKey(verbose_name='作者',to='UserInfo',to_field='nid',null=True)
    # 与分类的关系，一个分类对应多篇文章，一篇文章对应一个分类
    category=models.ForeignKey(to='Category',to_field='nid',null=True)
    # 与标签的关系，一个标签对应多篇文章，一篇文章对应多个标签
    tags=models.ManyToManyField(
        to=Tag,
        # 中间模型，不自动生成多对多关系表，使用手动创建的关系表
        through='Article2Tag',
        through_fields='nid'
    )

class Article2Tag(models.Model):
    nid=models.AutoField(primary_key=True)
    article=models.ForeignKey(to='Article',to_field='nid')
    tags=models.ForeignKey(to='Tag',to_field='nid')

    class Meta:
        # 固定的联合为一列表变量名
        unique_together = [
            # 联合唯一，一篇文章不能对应重复标签
            ('article','tags')
        ]

    def __str__(self):
        # 返回article对象的title属性
        return self.article.title+'--'+self.tags.title

class ArticleUpDown(models.Model):
    nid=models.AutoField(primary_key=True)
    user=models.ForeignKey(to='UserInfo',to_field='nid',null=True)
    article=models.ForeignKey(to='Article',to_field='nid',null=True)
    is_up=models.BooleanField(default=True)

    class Meta:
        unique_together=[
            # 联合唯一，不允许同一用户对同一篇文章重复点赞
            ('user','article'),
        ]

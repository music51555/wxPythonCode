from django.db import models
from django.contrib.auth.models import AbstractUser

# 用户信息表。继承的AbstractUser类，本身就已经包含了username、password、email等字段，再额外的添加一些自定义的字段，实现自定义用户表，作为用户的接口表
class UserInfo(AbstractUser):
    nid=models.AutoField(primary_key=True)
    telephone=models.CharField(max_length=11,null=True,unique=True)
    avatar=models.FileField(upload_to='avatars/',default='/avatars/default.png')
    # verbose_name指明一个易于理解和表述的对象名称, /vɝ'bos/  冗长的；啰嗦的
    create_time=models.DateTimeField(verbose_name='创建时间',auto_now_add=True)
    # 与Blog表是一对一的关系，一对一关系在哪张表中建立关系都是可以的，看更倾向于通过哪张表作为源头去查找
    blog=models.OneToOneField(to='Blog',to_field='nid',null=True,on_delete=True)

    def __str__(self):
        return self.username

class Blog(models.Model):
    # 博客信息表也是站点表，一个用户对应一个博客，这三个属性也可以放在用户表中，但是为了解耦，可以单独存放
    nid=models.AutoField(primary_key=True)
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
    blog=models.ForeignKey(verbose_name='所属博客',to='Blog',to_field='nid',on_delete=True)

    def __str__(self):
        return self.title

class Tag(models.Model):
    nid=models.AutoField(primary_key=True)
    title=models.CharField(verbose_name='标签名称',max_length=32)
    blog=models.ForeignKey(verbose_name='所属博客',to='Blog',to_field='nid',on_delete=True)

    def __str__(self):
        return self.title

class Article(models.Model):
    # 基础字段
    nid=models.AutoField(primary_key=True)
    title=models.CharField(verbose_name='文章标题',max_length=50)
    desc=models.CharField(verbose_name='文章描述',max_length=255)
    create_time=models.DateTimeField(verbose_name='创建时间',auto_now_add=True)
    content=models.TextField(verbose_name='文章详情')

    # 增加三个字段，用来存储评论数、点赞数和踩赞数。以后在查询某篇文章的评论数时，就会涉及到跨表查询，相比于添加操作和查询操作，跨表查询的效率会很低，所以每有一个新评论时，就在文章表中评论数列中+1
    comment_count=models.IntegerField(default=0)
    up_count=models.IntegerField(default=0)
    down_count=models.IntegerField(default=0)

    # 与用户的关系，一个用户对应多篇文章，一篇文章对应一个用户，多对多关系在多的表中创建关系
    user=models.ForeignKey(verbose_name='作者',to='UserInfo',to_field='nid',null=True,on_delete=True)
    # 与分类的关系，一个分类对应多篇文章，一篇文章对应一个分类
    category=models.ForeignKey(to='Category',to_field='nid',null=True,on_delete=True)
    # 与标签的关系，一个标签对应多篇文章，一篇文章对应多个标签
    tags=models.ManyToManyField(
        to='Tag',
        # 中间模型，不自动生成多对多关系表，使用手动创建的关系表
        through='Article2Tag',
        # 设置多对多的关系列，article列和tag列相互约束
        through_fields=('article','tag')
    )

    def __str__(self):
        return self.title

class Article2Tag(models.Model):
    nid=models.AutoField(primary_key=True)
    article=models.ForeignKey(to='Article', to_field='nid', on_delete=True)
    tag=models.ForeignKey(to='Tag', to_field='nid', on_delete=True)

    class Meta:
        # 固定的联合为一列表变量名
        unique_together = [
            # 联合唯一，一篇文章不能对应重复标签
            ('article','tag')
        ]

    def __str__(self):
        # 返回article对象的title属性
        return self.article.title+'--'+self.tag.title

class ArticleUpDown(models.Model):
    nid=models.AutoField(primary_key=True)
    user=models.ForeignKey(to='UserInfo',to_field='nid',null=True,on_delete=True)
    article=models.ForeignKey(to='Article',to_field='nid',null=True,on_delete=True)
    is_up=models.BooleanField(default=True)

    class Meta:
        unique_together=[
            # 联合唯一，不允许同一用户对同一篇文章重复点赞
            ('user','article'),
        ]

class Comment(models.Model):
    # 基础字段
    nid=models.AutoField(primary_key=True)
    user=models.ForeignKey(to='UserInfo',to_field='nid',on_delete=True)
    article=models.ForeignKey(to='Article',to_field='nid',on_delete=True)
    content=models.CharField(verbose_name='评论内容',null=True,max_length=255)

    # 如果只定义基础字段存储每一条评论，那么当有子级评论时，就无法确定父级评论是谁，所以添加parent_comment字段存储父级字段，为了起到约束的作用，使用ForeignKey，对于子级表中的字段，可以使用Comment，也可以是self，null=True表示评论为根评论，也是就是对文章的评论，而不是对评论的评论
    parent_comment=models.ForeignKey('self',null=True,on_delete=True)

    def __str__(self):
        return self.content

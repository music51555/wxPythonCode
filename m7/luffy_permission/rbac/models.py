from django.db import models
from django.contrib.auth.models import AbstractUser

class Menu(models.Model):
    '''
    一级菜单
    '''
    title = models.CharField(verbose_name='菜单名称',max_length=20)
    icon = models.CharField(verbose_name='图标',max_length=20)

    def __str__(self):
        return self.title


class Permission(models.Model):
    """
    权限表
    """
    title = models.CharField(verbose_name='标题', max_length=32)
    url = models.CharField(verbose_name='含正则的URL', max_length=128)
    icon = models.CharField(verbose_name='图标',max_length=20)
    pid = models.ForeignKey(verbose_name='父类菜单ID',to='self',to_field='id',blank=True,null=True,
                            help_text='父类菜单的ID，如果ID为None，那么就是菜单，如果不为None那么就是按钮',
                            on_delete=True)

    menu = models.ForeignKey(
        verbose_name='父级菜单',to='Menu',to_field='id',null=True,blank=True,help_text='如果非空，表示父节点序号，如果为空表示不是二级菜单',
        on_delete=True
    )

    def __str__(self):
        return self.title


class Role(models.Model):
    """
    角色
    """
    title = models.CharField(verbose_name='角色名称', max_length=32)
    permissions = models.ManyToManyField(verbose_name='拥有的所有权限', to='Permission', blank=True)

    def __str__(self):
        return self.title


class UserInfo(AbstractUser):
    """
    用户表
    """
    email = models.CharField(verbose_name='邮箱', max_length=32)
    roles = models.ManyToManyField(verbose_name='拥有的所有角色', to='Role', blank=True)

    def __str__(self):
        return self.username

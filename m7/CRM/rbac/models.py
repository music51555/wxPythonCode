from django.db import models
from django.contrib.auth.models import AbstractUser
from django.forms import widgets

class Permission(models.Model):
    nid = models.AutoField(primary_key=True)
    title = models.CharField(verbose_name='权限名称', max_length=32)
    url = models.CharField(
        verbose_name='含正则的URL',
        max_length=128)

    def __str__(self):
        return self.title


class Role(models.Model):
    nid = models.AutoField(primary_key=True)
    title = models.CharField(verbose_name='角色名称', max_length=50)

    permissions = models.ManyToManyField(
        verbose_name='拥有的所有权限',
        to='Permission',
        blank=True,
    )

    def __str__(self):
        return self.title

class UserInfo(AbstractUser):
    nid = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name='用户名', max_length=32)
    password = models.CharField(verbose_name='密码',max_length=64)
    email = models.EmailField(
        verbose_name='邮箱',
        max_length=32
    )
    roles = models.ManyToManyField(
        verbose_name='拥有的所有角色',
        to='Role',
        blank=True,
    )

    def __str__(self):
        return self.name
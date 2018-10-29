from django.db import models

class Book(models.Model):
    # AutoField表示自增长，等同于auto_increment,primary_key=True表示是否是主键
    id = models.AutoField(primary_key=True)
    # CharField表示字符串，等同于varchar，max_length表示最大字符长度
    title = models.CharField(max_length=32)
    # BooleanField表示布尔类型
    state = models.BooleanField()
    # DateField表示日期类型
    pub_date = models.DateField()
    # DecimalField数值类型，max_digits表示有几位数字，decimal_places表示有几位小数
    price = models.DecimalField(max_digits=8, decimal_places=2)
    publish = models.CharField(max_length=32)
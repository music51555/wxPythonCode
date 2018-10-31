将python代码转换成sql语句，根据编写的python代码和配置，可以将语句执行在各类数据库上，减少了对不同类型数据的不同语句进行编写

只能对标和数据操作，无法对数据库进行操作



####  1、models.py下编写ORM代码

```python
from django.db import models

#ORM创建表就是定义一个类，继承与models.Model,没有逗号分隔！！！
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
```



#### 2、settings.py下写数据库连接配置

```python
# mysql数据库引擎的配置
DATABASES = {
    'default': {
         # mysql数据库的引擎配置
        'ENGINE': 'django.db.backends.mysql',
         # 数据库名称
        m6Nishi458_2m6Nishi458_2
         # 用户名
        'USER':'root',
         # 密码
        'PASSWORD':'Nishi458_2',
         # 连接地址
        'HOST':'127.0.0.1',
         # 端口
        'PORT': 3306,
    }
}
```



#### 3、在settings.py文件中配置INSTALLED_APP应用

```python
INSTALLED_APPS = [
    'app01.apps.App01Config',
]
```



#### 4、Django默认的数据库接口是mysqldb，但对于python3.0以上的版本会有问题，所以在在init.py下添加import

```python
# 在项目的__init__.py文件中添加，如果没有填写会报错“django.core.exceptions.ImproperlyConfigured: Error loading MySQLdb module.Did you install mysqlclient?”
import pymysql
pymysql.install_as_MySQLdb()
```



#### 5、如果想在控制台打印生成的sql语句，在settings.py文件的任意位置添加

```python
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console':{
            'level':'DEBUG',
            'class':'logging.StreamHandler',
        },
    },
    'loggers': {
        'django.db.backends': {
            'handlers': ['console'],
            'propagate': True,
            'level':'DEBUG',
        },
    }
}
```



#### 6、在控制台执行语句创建表

```cmd
#执行语句后，在控制台输入打印生成的sql语句，执行完毕后，在数据库中查询到book表
python manage.py makemigrations
python manage.py migrate
```



#### 备选7、Django2.0如果使用python3.4以上的版本会报错，需要注释

```
如果报错
django.core.exceptions.ImproperlyConfigured: mysqlclient 1.3.3 or newer is required; you have 0.7.11.None

在路径C:\Programs\Python\Python36-32\Lib\site-packages\Django-2.0-py3.6.egg\django\db\backends\mysql文件中

把if version < (1, 3, 3):
     raise ImproperlyConfigured("mysqlclient 1.3.3 or newer is required; you have %s" % Database.__version__)注释
```



```python
#转换后变为如下语句
CREATE TABLE `app01_book` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `title` varchar(32) NOT NULL, `state` bool NOT NULL, `pub_date` date NOT NULL, `price` numeric(8, 2) NOT NULL, `publish` varchar(32) NOT NULL); 
```


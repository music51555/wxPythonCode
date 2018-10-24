#### 1、下载和安装django

```
pip3 install django==2.0.1
```

#### 2、新建django项目

```python
#在指定文件夹中新建django项目
django-admin.py startproject mysites
```

创建项目后会生成mysites文件夹，在文件夹中也包含mysites文件夹，与项目名一致，但可以改为其他名称，用于存放与项目相关的文件

![django创建项目](.\images\django创建项目.png)

`mysites文件夹：`

`setting.py`：全局配置文件

`urls.py`：路由控制

`wsgi.py`：封装了socket

![项目文件夹内容](.\images\项目文件夹内容.png)

#### 3、创建应用：

在项目文件夹中创建应用，一个项目可以包含多个应用，一个应用可以放在多个项目中

`manager.py`：控制django启动，创建app

```python
#创建应用，startpapp创建一个应用
python3 manage.py startapp blog
```

创建完成后，应用文件夹包含：

`views.py`存放函数视图代码

`models.py`存放与数据库连接代码

![django应用文件夹内容](.\images\django应用文件夹内容.png)

#### 4、创建templates

`templates文件夹`：存放html文件

![templates](.\images\templates.png)

#### 5、请求顺序

1、由urls.py根据请求路径进行路由分发

2、在views.py中执行视图函数

3、如果需要与数据库连接，则models.py中执行代码

4、templates中存放返回给用户的html网页

#### 6、项目与应用的关系：

微信项目中包含聊天、支付、朋友圈等应用

#### 7、启动Django

```python
#表示在本机指定了8865端口，如果不指定默认8000端口，http://127.0.0.1:8000/
python3 manage.py runserver 8865
```
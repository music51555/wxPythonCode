django

最主要的web框架

**MVC模型**：数据驱动视图

Model，数据库相关

View，存HTML文件

Control，处理逻辑

**MTV模型**

Model，模型，负责业务对象和数据库的关系映射(ORM) 

Template，模板，存放html文件，负责如何把页面展示给用户

View，视图，负责调用函数的业务逻辑 

1、浏览器发起请求后，由控制器urls.py进行路由分发（URL分发器），根据URL路径决定调用哪个函数

2、在view.py中查找函数，执行函数

3、可选（如果需要连接数据库，在models.py中连接数据库）

4、在tempale中查找html页面，返回给用户


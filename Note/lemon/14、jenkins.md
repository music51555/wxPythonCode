jenkins

CI：持续集成

CD：持续发布



作用：

部署测试环境

运行定时任务



**`msi`包**: 如果服务器是`windows`的会安装到`services.msc`中，

**`war`包**: 如果服务器是`linux`的，安装环境需要安装`JDK`，将`war`包部署到`Tomcat`中，放置在`webapps`中或指定路径

```
yum list java*
yum install ...
```



启动服务后，在提示路径中查看密码

```
cat /root/.jenkins/secrets/initialAdminPassword
```



构建项目后在工作目录中会生成当前项目的工作空间
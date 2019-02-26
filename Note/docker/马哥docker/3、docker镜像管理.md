docker 码头工人

镜像：应用程序的集装箱

镜像采用分层构建机制

`bootfs`：用于系统引导的文件系统，包括`bootloader`和`kernel`，容器启动后会被卸载以节约内存资源

镜像的文件系统`Aufs`，`3.18`开始引入`overlay2`

启动容器时，会先从本地获取镜像，如果没有则会从`Registry`中下载镜像到本地

一个镜像可以有多个`TAG`，但一个`TAG`只能属于一个镜像

`bash image`是由`dockerhub`的工作人员制作的

`quay.io`第三方的`docker`镜像仓库，如果不指定镜像地址，那么默认为`dockerhub`

通过容器制作镜像：

在容器启动时，通过`docker commit`来生成镜像

```shell
# -p参数表示执行暂停操作后，再提交为新的镜像
docker commit -p 1
```



`docker image`

```shell
#修改镜像标签，如果已经存在标签，则会为当前镜像再添加一个标签，成为一个新的镜像，删除时只是删除其景象引用
docker image tag xxxxx myhub/nginx:1.04
```



通过`docker inspect`查看容器启动默认执行的命令

```shell
# 在CMD中查看启动命令
docker inspect xxx
```



通过`docker commit`将容器保存为新的镜像

制作后的镜像包含在容器中创建的`/home/html/index.html`，并使用`-c`重新设置的容器启动命令启动了容器

```python
# 通过docker commit --help查看更多命令
# 通过-a 添加作者信息
# 通过-p 暂停容器，不暂停如果有读写中的文件，会存储为一半
# 通过-c 添加命令"CMD []"，在列表中添加命令，该参数要使用单引号括起来，不要使用双引号
docker commit -a "alex <452427904@qq.com>" -c 'CMD ["/bin/httpd","-f","-h","/home/html"]' -p da bh
```


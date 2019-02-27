`docker：`码头工人



**镜像：**应用程序的集装箱



##### 镜像采用分层构建机制：

##### `bootfs`：

这一层与我们典型的`Linux/Unix`系统是一样的 ，用于系统引导，包括`bootloader`和`kernel`，加载内核，容器启动后会被卸载以节约内存资源

##### `rootfs`：

在`bootfs`是`rootfs`层，`rootfs`就是各种不同的操作系统发行版，比如`Ubuntu，Centos`等 ，传统的`Linux`加载`bootfs`时会先将`rootfs`设为`read-only`，然后在系统自检之后将`rootfs`从`read-only`改为`read-write`。然后我们就可以在`rootfs`上进行写和读的操作 ，但`docker`在`bootfs`自检完毕之后并不会把`rootfs`的`read-only`改为`read-write`，利用`UnionFS`将一个或多个`read-only`的`rootfs`加载到之前的`read-only`的`rootfs`层之上 ，看起来只像一个文件系统 ，这些多层只读的`rootfs`被称为镜像，在`docker`对镜像执行`run`命令创建容器后，会在只读的`rootfs`之上分配一层空的`read-write`的`rootfs`，系统实际上是将这个在`read-only`层的`rootfs`的文件拷贝到`read-write`层的`rootfs`之中，然后对它进行修改，但`read-only`层的文件并不会被修改，依然存在于`read-only`层之中，只不过是在`read-write`层下被隐藏了，这是`unionFS`的特性 



镜像的文件系统是`Aufs`，`3.18`开始引入`overlay2`

启动容器时，会先从本地获取镜像，如果没有则会从`Registry`中下载镜像到本地

一个镜像可以有多个`TAG`，但一个`TAG`只能属于一个镜像

`base image`是由`dockerhub`的工作人员制作的

`quay.io`第三方的`docker`镜像仓库，如果不指定镜像地址，那么默认从`dockerhub`下载



##### 通过容器制作镜像：

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
docker commit -a "alex <452427904@qq.com>" -c 'CMD ["/bin/httpd","-f","-h","/home/html"]' -p bh busy_httpd:v0.2
```



##### 向`dockerhub`中`push`镜像

首先进行登录

```
docker login -u music51555
Password:
```



修改镜像和标签名称

```shell
# 将docker镜像名称修改为"dockerhub账户名/仓库名:TAG"
docker tag 87f8dd508d21 music51555/bh:latest
```



推送镜像

```
docker push music51555/bh:latest
```



拉取镜像

```shell
# 推送完成后，在music51555账户的bh仓库下，显示了多版本的镜像
docker pull music51555/bh
docker push music51555/bh:v0.2
```

![1551234976635](.\images\1551234976635.png)



`docker save`保存镜像文件

```shell
# docker save -o 保存的位置 镜像名称
# 自动将文件压缩
docker save -o bh.gz  music51555/bh music51555/bh:v0.2
```



`docker load`加载镜像文件

```shell
# docker load -i 加载文件的位置
# 自动读取压缩文件
docker load -i /home/hub/bh.gz
```


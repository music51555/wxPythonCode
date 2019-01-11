`docker`镜像



**获取镜像：**

通过`pull`命令默认从`docker-hub`仓库获取镜像：

**知识点1：**如果没有指定`TAG`版本，默认会选择`latest`标签，下载最新的

```
docker pull ubuntu:TAG
```

下载指定版本的`ubuntu`或`latest`版本

```
docker pull ubuntu:18.04
docker pull ubuntu:latest
```



**指定从哪`pull`获取镜像：**

**知识点1：**默认使用`pull`表示从`docker-hub`下载镜像

```shell
docker pull ubuntu:18.04

# 完整命令命令
docker pull registry.hub.docker.com/ubuntu:18.04
```



指定从**网易蜂巢**下载`ubuntu`镜像

```
docker pull hub.c.163.com/public/ubuntu:18.04
```



##### docker镜像默认存储位置

在`cd /var/lib/docker`





**docker run和docker exec的区别：**

`docker run`适用于在创建并运行容器时使用

`docker exec`适用于在已创建的容器上操作时使用



如：`docker run -it ubuntu:18.04 /bin/bash`表示创建一个容器，并启动一个`bash`会话

```shell
[root@VM_16_6_centos ~]# docker run -it ubuntu:18.04 /bin/bash
root@7f7cc8676eb8:/# ll
```



##### 在`dockerhub`镜像库中检索镜像

命令：

`docker search nginx `

`dockerhub`官网：

`https://hub.docker.com/search/?q=&type=edition&offering=community`

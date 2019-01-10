docker镜像



**获取镜像：**

通过pull命令从docker-hub仓库获取镜像：

知识点1：如果没有指定TAG版本，默认会选择latest标签，下载最新的

```
docker pull ubuntu:TAG
```

下载指定版本的ubuntu或latest版本

```
docker pull ubuntu:18.04
docker pull ubuntu:latest
```



**指定从哪pull获取镜像：**

知识点1：默认使用pull表示从docker-hub下载镜像

```shell
docker pull ubuntu:18.04

# 完整命令命令
docker pull registry.hub.docker.com/ubuntu:18.04
```



指定从网易蜂巢下载ubuntu镜像

```
docker pull hub.c.163.com/public/ubuntu:18.04
```



##### docker镜像默认存储位置

在`cd /var/lib/docker`









**docker run和docker exec的区别：**

docker run适用于在创建并运行容器时使用

docker exec适用于在已创建的容器上操作时使用



如：`docker run -it ubuntu:18.04 /bin/bash`表示创建一个容器，并启动一个bash会话

```shell
[root@VM_16_6_centos ~]# docker run -it ubuntu:18.04 /bin/bash
root@7f7cc8676eb8:/# ll
```





##### 在`dockerhub`镜像库中检索镜像

命令：

`docker search nginx `

`dockerhub`官网：

`https://hub.docker.com/search/?q=&type=edition&offering=community`



##### 配置docker加速器

提升国内用户访问 Docker Hub 拉取镜像的速度及稳定性，下载速度

`https://www.daocloud.io/mirror`

执行一条脚本即可

```
curl -sSL https://get.daocloud.io/daotools/set_mirror.sh | sh -s http://f1361db2.m.daocloud.io
```



##### 查看配置的加速器

会从这个国内的地址下载，时常会进行更新

```shell
cat /etc/docker/daemon.json
{"registry-mirrors": ["http://f1361db2.m.daocloud.io"]}
```



##### 查看docker镜像

```
docker images
```




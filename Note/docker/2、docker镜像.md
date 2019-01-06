docker镜像

##### 什么是镜像：

分层存储的文件，可以在一个镜像的上层创建多个容器

易于扩展

优化存储空间，是一个不包含linux内核，而又精简的linux系统



##### docker镜像默认存储位置

在`cd /var/lib/docker`



##### 在镜像库中检索镜像

命令：docker search nginx 

图形界面镜像库：

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



创建一个容器，就是在容器上创建一个读写层，如果在容器中修改一个文件，是在读写层copy一份儿镜像中的文件来进行修改的，不是修改原有文件

一个镜像可以创建多个容器，在容器中的改动不会影响镜像
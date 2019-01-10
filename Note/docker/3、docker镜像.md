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



**列出所有docker镜像：**

以下两种方式均可

```shell
docker images

[root@VM_16_6_centos ~]# docker image ls

#镜像名称             版本信息              镜像ID              镜像的最后更新时间     镜像大小 
 REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
 hello               latest              fce289e99eb9        8 days ago          1.84kB
 hello-world         latest              fce289e99eb9        8 days ago          1.84kB
 nginx               latest              7042885a156a        11 days ago         109MB
 ubuntu              18.04               1d9c17228a9e        11 days ago         86.7MB

```



**过滤查询镜像：**

```shell
# 添加-f参数可以过滤镜像结果，如dangling=true表示列出没有被使用的镜像
docker images -f dangling=true

docker image ls -f dangling=true
```



**为镜像添加标签**

为了日后方便查找，为已存在的镜像添加一个标签，但是新标签镜像和源镜像的id是一样的，也起到了类似链接的作用，把ubuntu:18.04 改名为myubuntu:18.04



```shell
docker tag ubuntu:18.04 myubuntu:18.04

[root@VM_16_6_centos ~]# docker image ls
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
myubuntu            18.04               1d9c17228a9e        11 days ago         86.7MB
ubuntu              18.04               1d9c17228a9e        11 days ago         86.7MB
```



**查看镜像的详细信息：**

知识点1：返回的结果是一个JSON格式

知识点2：如果只想查看JSON中的某项数据，通过-f选项过滤数据

```shell
docker inspect ubuntu:18.04

docker inspect -f {{".Config"}} ubuntu:18.04 
```



**通过history查看镜像各层的创建信息**

知识点1：查询出的内容如果过长会被截断，使用--no-trunc参数展示全部内容，不截断

```
docker history ubuntu:18.04 --no-trunc
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




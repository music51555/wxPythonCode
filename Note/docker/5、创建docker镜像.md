docker创建镜像

##### 1、基于已有的容器创建镜像

知识点1：创建容器命令`docker run -it ubuntu:18.04 /bin/bash`

知识点2：根据当前容器创建一个新的镜像`docker commit -m "xxx" -a "xxx" 容器ID 容器名称 容器TAG`

知识点3：-m参数表示提交进项的信息，-a表示镜像的作者信息

```shell
# 根据镜像名称和TAG创建一个容器，并启动一个bash会话
docker run -it ubuntu:18.04 /bin/bash

# 进入创建的容器后，如果做了许多修改，那么就可以根据当前容器创建一个新的镜像
docker commit -m "add test file" -a "wangxin" 7f7 test:0.1

# 再次查询所有镜像，列出了新创建的镜像
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
test                0.1                 9078b8d4b255        4 seconds ago       86.7MB
```



##### 2、根据openvz提供的模板创建镜像

访问https://download.openvz.org/template/precreated/地址后，下载tar包

通过命令创建

```shell
cat xxx.tar.gz | docker import - NAME:TAG
```



3、基于Dockerfile创建
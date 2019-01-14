创建`docker`容器

**知识点1：**通过`docker create -it ubuntu:18.04`来创建容器

**知识点2：**新建的容器状态是`Created`状态，需要使用`docker start 容器ID `来启动它

**知识点3：**通过`docker start 容器ID `启动容器，启动后状态变为`Up 20 seconds`

**知识点4：**在创建容器时，使用`--name`参数，为容器设置容器名称

**知识点5：**`docker run`和`docker create`的区别是一个创建容器并启动，一个只创建不启动

**知识点6：**当执行`docker run -it xxxx`来创建容器时，容器的状态显示为`Existed`退出状态，所以使用`docker run -itd xxxx`来创建容器，其中`-d`表示在后台运行

**知识点7**：`docker run -d -P nginx:latest`启动`nginx`镜像,并通过`-P`指定随机端口，`-p 8001`设置指定端口，通过`docker ps -a`查询进程后，使用`curl 127.0.0.1:xxxx`通过指定端口访问页面

```shell
docker create -it --name ubuntu-test ubuntu:18.04

# 创建后通过docker ps -a查询出新建的容器进程
[root@VM_16_6_centos ~]# docker ps -a
CONTAINER ID        IMAGE               COMMAND             CREATED              STATUS              PORTS               NAMES
fe840be98946        ubuntu:18.04        "/bin/bash"         About a minute ago   Created                                 objective_turing
```


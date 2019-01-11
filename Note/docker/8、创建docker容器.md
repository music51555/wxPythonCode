创建`docker`容器

**知识点1：**通过`docker create -it ubuntu:18.04`来创建容器

**知识点2：**新建的容器状态是`Created`状态，需要使用`docker start 容器ID `来启动它

**知识点3：**通过`docker start 容器ID `启动容器，启动后状态变为`Up 20 seconds`

**知识点4：**在创建容器时，使用`--name`参数，为容器设置容器名称

**知识点5：**`docker run`和`docker create`的区别是一个创建容器并启动，一个只创建不启动

```shell
docker create -it --name ubuntu-test ubuntu:18.04

# 创建后通过docker ps -a查询出新建的容器进程
[root@VM_16_6_centos ~]# docker ps -a
CONTAINER ID        IMAGE               COMMAND             CREATED              STATUS              PORTS               NAMES
fe840be98946        ubuntu:18.04        "/bin/bash"         About a minute ago   Created                                 objective_turing
```


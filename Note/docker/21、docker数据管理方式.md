docker数据管理方式：

1、数据卷：容器内的数据直接映射到本地主机环境

2、数据卷容器：使用特定容器维护数据卷

3、绑定数据卷：在创建容器时将主机本地的任意路径挂在到容器内作为数据卷



创建数据卷：

```shell
docker run -d --name devtest --mount source=test,target=/app nginx:latest
```

删除数据卷:

```
docker stop xxx
docker rm xxx
docker volume ls
docker volume rm xxx
```



创建服务时添加卷

```shell
docker service create -d --replicas=3 --name devtest --mount source=myvol2,target=/app nginx:latest 
```


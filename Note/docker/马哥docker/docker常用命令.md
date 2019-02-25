docker常用命令



docker search

```shell
# 其中alpine表示微型小镜像
搜索镜像
```



docker image pull

```shell
下载一个镜像
docker image pull nginx:1.14-alpine
```



docker image ls

```shell
查看镜像列表

# 使用docker image ls --help查看更多命令
docker image ls --no-trunc
```



docker image rm xxx

```
删除docker镜像
```



docker container --help查看更多命令



docker container start/stop

```shell
启动或停止容器

# docker container start -ai表示支持标准的输入输出启动容器
```



docker container run/docker run

只有在需要运行shell的时候，才需要添加-it参数，启动服务，如nginx，只需要使用-d即可

```shell
# 创建并启动一个容器
# -t 分配一个交互式终端
# -i 指定标准输入
# --name 给容器起名
# --rm 容器停止后自动删除
# -d在后台运行

# 启动后 进程PID为1的进程为命令运行进行，如果通过exit退出容器后，那么容器也就停止了
docker run --name busybox -it busybox

# 如果run的镜像本地没有，会通过镜像加速器自动下载
docker run --name web1 -d nginx
```



docker container ls/docker ps -a

```shell
查看容器列表
# 其中COMMAND表示在容器中运行的命令，每一个容器都有需要运行的一个程序
```



docker container pause/unpause

```
暂停或解除暂停容器
```



docker container rm

```
删除容器
```



docker exec

查看容器内是如何运行的

启动一个容器进程后，可以通过docker container exec来运行另一个命令，如/bin/sh，退出后容器依然正常运行，不会结束

```shell
# 在容器中运行另一个进程，运行sh的shell

docker exec -it /bin/sh
```



netstat -ntl

```
在linux中查看端口监听情况
```



docker logs

如何容器内只启动一个进程，那么通过docker logs直接将日志输出到控制台



控制容器使用内存，如果超出会被OOM KILL掉容器进程

```shell
# -m表示限制使用内存大小  --memory-swap表示交换内存为物理内存的2倍,-1表示使用宿主机的交换内存
docker run --name web1  -m 300M --memory-swap -1 -d nginx
```




linux内核支持6种名称空间

UTS、User(各自的用户)、Mount(各自挂载的文件系统)、IPC、Pid(各自的PID)，Net



docker提供了4种网络

bridge：docker0，软交换机，网卡，容器启动后，容器内的网卡连接到docker0上

host：让容器使用宿主机的名称空间

none：没有网卡的容器，不需要进行网络通信，处理数据时需要运行的容器

open container：共享物理机的网络名称空间，连接物理机的其他通信计算机



docker network ls

```
# 查看docker网络类型
docker network ls

# 查看bridge网络类型的信息
docker network inspect bridge

```



默认创建的容器网络类型为bridge，有eth0网卡

```shell
# --rm参数表示容器
# 添加--network bridge表示手动指定容器的网络类型
# 默认hostname为容器id，使用--hostname设置主机名，cat /etc/hosts
# --dns设置容器的dns服务器，cat /etc/resolv.conf
# --add-host www.baidu.com:1.1.1.1
docker run --name b1 -it --network bridge --hostname mybusybox --dns 114.114.114.114 --rm busybox:latest
```



25分钟
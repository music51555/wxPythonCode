##### 安装依赖包

```shell
yum install -y yum-utils \
  device-mapper-persistent-data \
  lvm2
```



##### 设置`yum`源

```shell
yum-config-manager \
    --add-repo \
    https://download.docker.com/linux/centos/docker-ce.repo
```



##### 查看`yum`源

```shell
ls /etc/yum.repos.d/docker-ce.repo
```



##### 通过`yum`安装`docker`

```shell
yum install docker-ce -y
```



##### 启动`docker`，并设置开机启动

```shell
systemctl start docker
systemctl enable docker
```



##### 测试输出`hello-world`，如果没有镜像会下载

```shell
docker run hello-world
```



##### 查看`docker`信息

展示镜像、容器数量等信息、`docker`版本等信息概览

```shell
docker info
[root@VM_16_6_centos ~]# docker info
Containers: 3
 Running: 1
 Paused: 0
 Stopped: 2
Images: 4
Server Version: 18.09.0
Storage Driver: overlay2
```



##### 查看`docker`版本

```shell
docker version
```

安装依赖包

```shell
yum install -y yum-utils \
  device-mapper-persistent-data \
  lvm2
```



设置yum源

```shell
yum-config-manager \
    --add-repo \
    https://download.docker.com/linux/centos/docker-ce.repo
```



查看yum源

```shell
ls /etc/yum.repos.d/docker-ce.repo
```



安装docker

```shell
yum install docker-ce -y
```



启动docker，并设置开机启动

```shell
systemctl start docker
systemctl enable docker
```



测试输出hello-world，如果没有镜像会下载

```shell
docker run hello-world
```



查看docker信息

```
docker info
```



查看docker版本

```shell
docker version
```



下载并创建容器

```shell
# -it表示在前台运行
docker run -it nginx
```



查看容器状态

```
docker ps
```



检查容器，可以查看容器ip ，美  [ɪn'spɛkt]  检查

```
docker inspect 容器id
```



访问nginx容器的主页

```
curl IP
```



进入容器

```shell
docker exec -it 容器ID bash
root@a55cce2dc36f:/# ls
bin   dev  home  lib64	mnt  proc  run	 srv  tmp  var
boot  etc  lib	 media	opt  root  sbin  sys  usr
```


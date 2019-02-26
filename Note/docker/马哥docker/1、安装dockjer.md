在vim中如何进行全文替换

```
:%s@目标文本@替换文本
```



##### 安装docker

在清华大学`docker`镜像站中找到`docker-ce`

```
https://mirrors.tuna.tsinghua.edu.cn/
```

依次在路径`docker-ce/linux/centos/`下拷贝`docker-ce.repo`的链接地址，使用`wget`命令下载`docker-ce`仓库

```
wget https://mirrors.tuna.tsinghua.edu.cn/docker-ce/linux/centos/docker-ce.repo
```

使用`vim`命令查看，修改配置文件的下载路径

```
:%s@https://download.docker.com/@https://mirrors.tuna.tsinghua.edu.cn/docker-ce/
```

查看可用的仓库中是否有`!docker-ce-stable/x86_64`

```
yum repolist
```

安装`docker`

```
yum install docker-ce
```



##### 创建配置文件，配置镜像加速器

在`/etc/docker/`下创建`daemon.json`文件，配置镜像加速器，写入配置

```
{
	"registry-mirrors": ["https://registry.docker-cn.com"]
}
```



##### 查看`docker`版本信息

```shell
# 其中显示了客户端和服务端的API版本，GO版本等信息
# 更详细的信息使用docker info命令，其中显示了加速器等信息
docker version

Client:
 Version:           18.09.0
 API version:       1.39
 Go version:        go1.10.4
 Git commit:        4d60db4
 Built:             Wed Nov  7 00:48:22 2018
 OS/Arch:           linux/amd64
 Experimental:      false

Server: Docker Engine - Community
 Engine:
  Version:          18.09.2
  API version:      1.39 (minimum version 1.12)
  Go version:       go1.10.6
  Git commit:       6247962
  Built:            Sun Feb 10 03:47:25 2019
  OS/Arch:          linux/amd64
  Experimental:     false
```




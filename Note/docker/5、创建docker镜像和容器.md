docker创建容器

##### 1、创建并运行容器

**知识点1：**创建容器命令`docker run -it ubuntu:18.04 /bin/bash`，表示创建一个容器，并打开`bash`会话

**知识点2：**`-i`表示保存容器内的stdin标准输入是开启的，保证了向伪终端内持久的输入

**知识点3：**`-t`表示在创建容器时提供一个交互式的`shell`



```shell
# 根据镜像名称和TAG现在本地查找镜像，如果没有则会在dockerhub中检索、下载镜像，下载完成后创建为一个容器，并启动一个bash会话
docker run -it ubuntu:18.04 /bin/bash

Unable to find image 'ubuntu:latest' locally
latest: Pulling from library/ubuntu
38e2e6cd5626: Pull complete 
705054bc3f5b: Pull complete 
c7051e069564: Pull complete 
7308e914506c: Pull complete 
Digest: sha256:f0509fb8b4a9d92017531669367b93978a7aeb47429cfc5a0f723859cf00e65f
Status: Downloaded newer image for ubuntu:latest
root@22c6f32d1ffa:/# 在此可以输入命令
```



此时在容器内查看主机配置

```shell
# docker已经为容器的IP，添加了一条主机配置
cat /etc/hosts
127.0.0.1       localhost
::1     localhost ip6-localhost ip6-loopback
fe00::0 ip6-localnet
ff00::0 ip6-mcastprefix
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters
172.17.0.3      22c6f32d1ffa
```



##### 2、查看容器状态

**知识点1：**当通过`exit`退出容器的`bash`终端后，容器的运行状态变为`Exited`

**知识点2：**通过`docker start 22c`来重新启动容器

**知识点3：**重新启动`Exited`的容器后，可以通过`docker attach 22c`来重新附着到该运行的容器上

```shell
docker attach ubuntu-test
root@d6587800c2f3:/# 
```





##### 3、重命名docker容器

**知识点1：**启动容器后，会随机分配一个容器名称，如`elastic_hoover`，在启动时可以通过`—name`来命名容器

```shell
docker run -it --name ubuntu-test ubuntu:latest

CONTAINER ID   IMAGE            COMMAND       CREATED        STATUS       PORTS      NAMES
d6587800c2f3   ubuntu:latest    "/bin/bash"   8 seconds ago  Exited (0) 2 seconds ago                            ubuntu-test
```





##### 4、创建守护进程容器

**知识点1：**添加`-d`参数，将容器在后台运行

**知识点2：**在后台运行，并一直执行程序的的容器状态是`Up`运行中

```shell
docker run -d --name ubuntu-test ubuntu /bin/sh -c "while true;do echo hello world;sleep 1;done"
```



##### 5、查看容器日志

**知识点1：**通过`docker logs xxx`来查看容器日志

```shell
docker logs ubuntu-test 
hello world
hello world
hello world
```



##### 6、持续查看容器日志

**知识点1：**通过`docker logs -f xxxx`添加`-f`参数获取所有的日志内容后，在持续查看最新的日志，类似于`tail -f`来持续查看容器日志



##### 7、持续查看最新的日志

**知识点1：**通过`docker logs --tail 0 -f ubuntu-test`来持续的查看最新输出的日志，而不是只添加-f参数查看所有的日志，而是只输出最新的日志

**知识点2：**只查看最后几行日志信息`docker logs --tail 10 ubuntu-test`



##### 8、以当前容器创建一个新的镜像

**知识点1：**根据当前容器创建新镜像`docker commit -m "xxx" -a "xxx" 容器ID 或 容器名称 新NAME：新TAG`

**知识点2：**`-m`参数表示提交进项的信息，-a表示镜像的作者信息

```shell
# 进入创建的容器后，如果做了许多修改，那么就可以根据当前容器创建一个新的镜像
docker commit -m "add test file" -a "wangxin" 7f7 test:0.1

# 再次查询所有镜像，列出了新创建的镜像
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
test                0.1                 9078b8d4b255        4 seconds ago       86.7MB
```



##### 9、创建`docker`而不运行容器

**知识点1：**通过`docker create -it ubuntu:18.04`来创建容器

**知识点2：**新建的容器状态是`Created`状态，需要使用`docker start 容器ID `来启动它

**知识点3：**通过`docker start 容器ID `启动容器，启动后状态变为`Up 20 seconds`

**知识点5：**`docker run`和`docker create`的区别是一个创建容器并启动，一个只创建不启动

**知识点6**：`docker run -d -P nginx:latest`启动`nginx`镜像,并通过`-P`指定随机端口，`-p 8001`设置指定端口，通过`docker ps -a`查询进程后，使用`curl 127.0.0.1:xxxx`通过指定端口访问页面

```shell
docker create -it --name ubuntu-test ubuntu:18.04

# 创建后通过docker ps -a查询出新建的容器进程
[root@VM_16_6_centos ~]# docker ps -a
CONTAINER ID        IMAGE               COMMAND             CREATED              STATUS              PORTS               NAMES
fe840be98946        ubuntu:18.04        "/bin/bash"         About a minute ago   Created                                 objective_turing
```



##### 10、在容器内启动额外的新进程

**知识点1：**通过`docker exec`命令在已启动的容器中，启动新的进程，同时也支持`-d`和`-it`参数

```shell
# 在后台运行新的进程和命令
docker exec -d ubuntu-test mkdir /home/wangxiaoxin

# 在前台运行新的进程和命令，开启的bash后，就可以运行其他命令了
docker exec -it ubuntu-test /bin/bash

root@448aa849817c:/# cd /home
root@448aa849817c:/home# ls
wangxiaoxin
```



##### 11、停止容器

**知识点1：**通过`docker stop xxx`和`docker kill xxx`来停止容器，区别是一个是发送`SIGTERM`信号，一个是发送`SIGKILL`信号



##### 2、根据`openvz`提供的模板创建镜像

访问`https://download.openvz.org/template/precreated/`地址后，下载tar包

通过命令创建

```shell
cat xxx.tar.gz | docker import - NAME:TAG
```



##### 3、基于`Dockerfile`创建
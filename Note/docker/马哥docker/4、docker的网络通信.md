`linux`内核支持6种名称空间

`UTS`、`User`(各自的用户)、`Mount`(各自挂载的文件系统)、`IPC`、`Pid`(各自的`PID`)，`Net`



`docker`提供了4种网络

`bridge`：`docker0`，软交换机，网卡，容器启动后，容器内的网卡连接到`docker0`上，与其他容器相互联通

`host`：让容器使用宿主机的名称空间

`none`：没有网卡的容器，不需要进行网络通信，处理数据时需要运行的容器

`open container`：共享物理机的网络名称空间，连接物理机的其他通信计算机



`docker network ls`

```shell
# 查看docker网络类型
docker network ls

# 查看bridge网络类型的信息
docker network inspect bridge
```



默认创建的容器网络类型为`bridge`，有`eth0`网卡

```shell
# --rm参数表示容器停止运行后，自动删除容器
# 添加--network bridge表示手动指定容器的网络类型
# 默认hostname为容器id，使用--hostname设置主机名，cat /etc/hosts
# --dns设置容器的dns服务器，cat /etc/resolv.conf
# --add-host www.baidu.com:1.1.1.1 添加/etc/hosts中的域名解析
docker run/create --name b1 -it --network bridge --hostname mybusybox --dns 114.114.114.114 --rm busybox:latest
```



暴露容器服务端口

```shell
# 运行容器后，暴露容器的80端口，动态的与宿主机的某个端口映射
docker run --name myweb -p 80 busybox_http

# 宿主机的80端口映射容器的80端口
docker run --name myweb -p 80：80 busybox_http

# 创建容器时，将ip配置设置为与容器b1的配置相同，如ip地址等
docker run --name myweb --network container:b1 busybox_http

# 使容器的网络配置使用宿主机的配置，这样就可以外网访问
docker run --name myweb --network host busybox_http

# --ip设置容器ip地址
docker run --name myweb --network host --ip 172.17.0.5 busybox_http

# 通过iptables -t nat -vnL来查看端口映射情况
# -t表示查看TCP端口
# -v表示详细信息
# -n表示以数字化显示
# -L表示以列表形式查看
iptables -t nat -vnL

# 查看主机端口开放情况
# -t TCP端口
# -n表示以数字化显示
# -L表示以列表形式查看
netstat -tnl

# 通过docker port来映射
docker port busybox_http
```



修改容器的默认`ip`地址和`dns`

```shell
# 修改docker配置文件 vim /etc/docker/daemon.json，并重启服务
{
    "registry-mirrors": ["https://registry.docker-cn.com"],
    # 表示16位掩码
    "bip":"10.0.0.1/16",
    "dns":["114.114.114.114","8.8.8.8"]
}

# 使用！vim可以打开上一次打开的文件
！vim

# 重启后docker0的信息被改变
docker0: flags=4099<UP,BROADCAST,MULTICAST>  mtu 1500
        inet 10.0.0.1  netmask 255.255.0.0  broadcast 10.0.255.255
        ether 02:42:4e:d0:75:a1  txqueuelen 0  (Ethernet)
        RX packets 13686  bytes 1021653 (997.7 KiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 15008  bytes 43006122 (41.0 MiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
```



远程连接其他服务器的`docker`

```shell
# 在/etc/docker/daemon.json
"hosts":["tcp://0.0.0.0:2375","unix:///var/run/docker.sock"]

# 通过docker -H 172.0.0.23:2375 ps查看其他计算机上的docker 信息
docker -H 172.0.0.23:2375 image ls
```


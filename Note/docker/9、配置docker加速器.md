配置docker加速器

##### 配置`docker`加速器

提升国内用户访问 `Docker Hub` 拉取镜像的速度及稳定性，下载速度

`https://www.daocloud.io/mirror`

执行一条脚本即可

```
curl -sSL https://get.daocloud.io/daotools/set_mirror.sh | sh -s http://f1361db2.m.daocloud.io
```



##### 查看配置的加速器

会从这个国内的地址下载，时常会进行更新

```shell
cat /etc/docker/daemon.json
{"registry-mirrors": ["http://f1361db2.m.daocloud.io"]}
```


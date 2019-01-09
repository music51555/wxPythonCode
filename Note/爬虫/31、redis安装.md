`redis`安装

下载、编译`redis`

```
wget http://download.redis.io/releases/redis-5.0.3.tar.gz
tar -zxvf redis-5.0.3.tar.gz
cd redis-5.0.3
```

出现如下错误使用`yum install gcc` ：

```
[root@localhost redis-4.0.11]# make
cd src && make all
make[1]: Entering directory `/root/redis-4.0.11
/src‘ CC adlist.o /bin/sh: cc: command not found make[1]: *** [adlist.o] Error 127 make[1]: Leaving directory `/root/redis-2.8.17/src‘ make: *** [all] Error 2
```

再次安装提示，使用`make MALLOC=libc `

```
[root@localhost redis-4.0.11]# make
cd src && make all
make[1]: Entering directory `/root/redis-2.8.17/src‘
    CC adlist.o
In file included from adlist.c:34:
zmalloc.h:50:31: error: jemalloc/jemalloc.h: No such file or directory
zmalloc.h:55:2: error: #error "Newer version of jemalloc required"
make[1]: *** [adlist.o] Error 1
make[1]: Leaving directory `/root/redis-2.8.17/src‘
make: *** [all] Error 2
```

在编译完成后，`src`文件夹内就有了可执行文件`redis-server`



启动`redis`

`./redis-server ../redis.conf`



启动客户端

`./redis-cli`



测试

```
set name alex

get name
```


docker常用选项：



比较容器和镜像的差异

docker container diff 镜像id



创建并进入容器，-i表示交互式，-t表示分配一个伪终端

docker run -it nginx



查看最新启动的容器

docker ps -l 



使容器在后台运行，前提是一个后台进程必须有一个前段进程，所以使用-itd选项，先在前端运行，再在后台运行

docker run -d nginx



查看容器进程

docker top 容器ID



为容器设置端口

在宿主机访问127.0.0.1:88端口时，就访问到了docker环境的nginx服务

docker container run -p 88:80 nginx



为容器设置主机名，较少使用

在容器内可通过hostname查看主机名

docker container run -h nginxhostname nginx



为容器设置环境变量

docker container run -e test=123456 nginx

进入容器后通过echo $test查看设置的变量



设置容器名称

docker container run -name nginxweb



查看容器日志

如在宿主机访问nginx服务后，可通过容器名称查看容器日志

docker logs web



进入容器

docker exec -it 容器ID/名称 bash



生成随机端口对应nginx服务，启动后可通过docker ps -l查看最新启动的容器信息，查看随机端口

docker container run -P nginx



重启宿主机后，docker会自动启动镜像

docker container run --restart always nginx


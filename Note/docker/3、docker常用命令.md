**docker常用命令：**

通过docker --help查看命令



**docker镜像管理命令**

docker image -help



docker image ls 或 docker image，列出所有镜像，TAG列表示版本



build 构建Dockerfile



history 查看镜像历史



inspect nginx 查看nginx容器的详细信息



pull nginx:least 或1.14下载最新版的nginx或1.14版本的nginx



push，推送到镜像仓库



rm，删除一个或多个镜像



prune，移除未使用的镜像 



tag，重新复制一份儿镜像，并起个别名



save，保存镜像到目标位置，发送给别人

docker image save nginx > nginx.tar



load，加载镜像

docker image load  < centos.tar
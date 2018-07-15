PID和PPID

通过导入OS模块，实现查看进程的PID，和父进程的PID

```python
import time
import os

from multiprocessing import Process

def func(name):
       print('%s is running,it is pid %s,it is parent pid %s'%(name,os.getpid(),os.getppid()))
       time.sleep(2)
       print('%s is done'%name)

if __name__ == '__main__':
       p = Process(target = func,args = ('子进程1',))
       p.start()

       print('主进程的PID是%s,主进程的父进程PID是%s'%(os.getpid(),os.getppid()))
       #或者通过对象的pid方法查看pid值
       print(p.pid)
#主进程的父进程ID是pycharm的进程ID号
'''
主进程的PID是1209,主进程的父进程PID是1120
子进程1 is running,it is pid 1210,it is parent pid 1209
子进程1 is done
'''
```


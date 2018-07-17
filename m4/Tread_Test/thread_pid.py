import os

from threading import Thread

def task(name):
    print('%s is running'%name)
    print('%s 的pid是 %s,ppid是%s'%(name,os.getpid(),os.getppid()))

if __name__ == '__main__':
    t = Thread(target = task,args = ('子线程1',))
    t.start()

    print('主线程的pid是%s'%os.getpid())
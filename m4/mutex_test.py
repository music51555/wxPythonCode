import time
import os
from multiprocessing import Process,Lock

def task(name,mutex):
    mutex.acquire()
    print('子进程的id是%s,子进程的父进程的id是%s'%(os.getpid(),os.getppid()))
    print('%s is running'%name)
    time.sleep(2)
    print('%s is done'%name)
    mutex.release()

if __name__ == '__main__':
    mutex = Lock()
    for i in range(3):
        p = Process(target = task,args = ('子进程%s'%i,mutex))
        p.start()

    print('主')
    print('主进程的id是%s,主进程的父进程id是%s'%(os.getpid(),os.getppid()))

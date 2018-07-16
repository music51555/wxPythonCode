import time

from multiprocessing import Process,Lock

def task(name,mutex):
    mutex.acquire()
    for i in range(3):
        time.sleep(1)
        print('%s is running to %s'%(name,i))
    mutex.release()

if __name__ == '__main__':
    mutex = Lock()
    p1 = Process(target = task,args = ('子进程1',mutex))
    p2 = Process(target = task,args = ('子进程2',mutex))
    p3 = Process(target = task,args = ('子进程3',mutex))
    p1.start()
    p2.start()
    p3.start()
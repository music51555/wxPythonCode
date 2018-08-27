import time
from multiprocessing import Process,Lock

def task(name,mutex):
    mutex.acquire()
    print('%s is running'%name)
    time.sleep(2)
    print('%s is done'%name)
    mutex.release()

if __name__ == '__main__':
    mutex = Lock()
    for i in range(3):
        p = Process(target=task,args=('子进程%s'%i,mutex))
        p.start()
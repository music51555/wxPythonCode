from threading import Thread,Semaphore
import time

def task(name,sm):
    sm.acquire()
    print('%s is running'%name)
    time.sleep(2)
    print('%s is done'%name)
    sm.release()

if __name__ == '__main__':
    sm = Semaphore(5)
    for i in range(10):
        t = Thread(target = task,args = ('子进程%s'%i,sm))
        t.start()

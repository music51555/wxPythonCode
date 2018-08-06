import time,random
from threading import Thread,Semaphore

def task(name,sm):
    with sm:
        print('%s is running'%name)
        time.sleep(random.randint(1,3))
        print('%s is done'%name)

if __name__ == '__main__':
    sm = Semaphore(5)
    for i in range(10):
        t = Thread(target = task,args = ('子线程%s'%i,sm))
        t.start()
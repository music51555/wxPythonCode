import time
from multiprocessing import Process

def task(name):
    print('%s is running'%name)
    time.sleep(2)
    print('%s is done'%name)

if __name__ == '__main__':
    p = Process(target = task,args = ('子进程1',))
    p.daemon = True
    p.start()

    print('主')
from threading import Thread
import time

def task(name):
    print('%s is running'%name)
    time.sleep(3)
    print('%s is done'%name)

def foo(name):
    print('%s is running'%name)
    time.sleep(1)
    print('%s is done'%name)

if __name__ == '__main__':
    t1 = Thread(target = task,args = ('子进程1',))
    t2 = Thread(target = foo,args = ('子进程2',))

    t1.daemon = True
    t1.start()
    t2.start()

    print('主线程')



import time
from threading import Thread,current_thread,active_count,enumerate

def task():
    print('%s is running'%current_thread().getName())
    time.sleep(3)
    print('%s is done'%current_thread().getName())

def foo():
    print('%s is running' % current_thread().getName())

if __name__ == '__main__':
    t1 = Thread(target=task,name='子进程1')
    t2 = Thread(target=foo,name='子进程2')
    t2.daemon=True
    t1.start()
    t2.start()
    time.sleep(1.5)
    print(enumerate())

    print('主')
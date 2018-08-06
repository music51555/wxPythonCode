from multiprocessing import Process,Array
import time

def task(name):
    print('%s is running'%(name,))
    for i in range(3):
        m[i] = i

def foo(name):
    time.sleep(5)
    print('%s is running'%(name,))
    for i in range(3,5):
        m[i] = i

if __name__ == '__main__':
    m = Array('i',5)
    p1 = Process(target = task,args = ('子进程1',))
    p2 = Process(target = foo,args = ('子进程2',))
    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print(m[:])
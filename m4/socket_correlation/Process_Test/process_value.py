from multiprocessing import Process,Value
import time

def task(name):
    time.sleep(5)
    print('%s is running,value is %s'%(name,res.value))

def foo(name):
    res.value -= 100
    print('%s is running,value is %s'%(name,res.value))

if __name__ == '__main__':
    res = Value('i',2000)

    p1 = Process(target = task,args = ('子进程1',))
    p2 = Process(target = foo,args = ('子进程2',))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
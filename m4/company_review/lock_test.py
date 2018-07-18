import time
from threading import Thread,RLock

mutexA = mutexB = RLock()

class MyThread(Thread):
    def __init__(self,name):
        super(MyThread,self).__init__()
        self.name = name

    def run(self):
        self.f1()
        self.f2()

    def f1(self):
        mutexA.acquire()
        print('%s得到A锁'%self.name)
        mutexB.acquire()
        print('%s得到B锁'%self.name)
        mutexA.release()
        print('%s释放A锁'%self.name)
        mutexB.release()
        print('%s释放B锁'%self.name)

    def f2(self):
        mutexB.acquire()
        print('%s得到B锁'%self.name)
        time.sleep(0.1)
        mutexA.acquire()
        print('%s得到A锁'%self.name)
        mutexB.release()
        print('%s释放B锁'%self.name)
        mutexA.release()
        print('%s释放A锁'%self.name)

if __name__ == '__main__':
    for i in range(3):
        m = MyThread('子线程%s'%i)
        m.start()
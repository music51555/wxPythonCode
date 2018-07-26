from multiprocessing import Process,Manager
import time

def task(d):
    d.append('haha')

def foo(d):
    time.sleep(2)
    print(d)

if __name__ == '__main__':
    m = Manager()
    d = m.list()
    p1 = Process(target = task,args = (d,))
    p2 = Process(target = foo,args = (d,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
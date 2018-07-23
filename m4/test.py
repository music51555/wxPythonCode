import os, random, time
from concurrent.futures import ProcessPoolExecutor


def task(name):
    print('%s is running,it is pid %s'%(name,os.getpid()))
    time.sleep(random.randint(1,5))

    print('%s is done'%name)


if __name__ == '__main__':
    p = ProcessPoolExecutor(5)
    for i in range(10):
        p.submit(task, '子进程%s'%i)

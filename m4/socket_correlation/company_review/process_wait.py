from concurrent.futures import ThreadPoolExecutor
import time,random,os

def task(name):
    print('%s is runing,it is pid %s'%(name,os.getpid()))
    time.sleep(random.randint(3,10))
    print('%s is done'%name)

if __name__ == '__main__':
    pool = ThreadPoolExecutor(2)
    pool.map(task,range(10))

    pool.shutdown(wait = False)
    print('主线程')
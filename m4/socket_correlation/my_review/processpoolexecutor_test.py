import time,random
from concurrent.futures import ThreadPoolExecutor

def task(name):
    print('%s is running'%name)
    time.sleep(random.randint(1,3))
    print('%s is done'%name)

if __name__ == '__main__':
    pool = ThreadPoolExecutor(5)
    for i in range(10):
        pool.submit(task,'子线程%s'%i)
    pool.shutdown()

    print('主进程')
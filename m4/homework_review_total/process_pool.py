# from concurrent.futures import ProcessPoolExecutor
# import time
#
# def task(name):
#     print('%s is running'%name)
#     time.sleep(2)
#     print('%s is done'%name)
#
# if __name__ == '__main__':
#     pool = ProcessPoolExecutor(5)
#     for i in range(10):
#         pool.submit(task,'子线程%s'%i)
#     # pool.shutdown()
#     print('主')

from concurrent.futures import ThreadPoolExecutor
from threading import current_thread
import time

def task():
    print('%s is running'%current_thread().getName())
    time.sleep(2)
    print('%s is done'%current_thread().getName())

if __name__ == '__main__':
    pool = ThreadPoolExecutor(5)
    for i in range(10):
        pool.submit(task)

# from concurrent.futures import ProcessPoolExecutor,ThreadPoolExecutor
# from threading import current_thread
# import time,random,os
#
# def task():
#     print('%s is running, it is pid %s'%(current_thread().getName(),os.getpid()))
#     time.sleep(random.randint(1,5))
#
# if __name__ == '__main__':
#     pool = ThreadPoolExecutor(4)
#     for i in range(10):
#         pool.submit(task)
#     #关闭进程池入口，不允许再开启进程，相当于join的操作
#     pool.shutdown(wait = True)
#
#     print('主进程')

from concurrent.futures import ProcessPoolExecutor,ThreadPoolExecutor
import time,random,os

def task(name):
    print('%s is running, it is pid %s'%(name,os.getpid()))
    time.sleep(random.randint(1,5))

if __name__ == '__main__':
    #如果没有设置进程数，那么默认为CPU的总核数
    pool = ProcessPoolExecutor(4)
    for i in range(10):
        #异步提交，提交任务后，不管任务是否启动，是否得到结果，直接提交
        pool.submit(task,'子进程%s'%i)
    #关闭进程池入口，不允许再开启进程，相当于join的操作，最后才运行主程序
    pool.shutdown(wait = True)

    print('主进程')

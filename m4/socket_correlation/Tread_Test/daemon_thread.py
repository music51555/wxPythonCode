# import time
# from threading import Thread
#
# def task(name):
#     print('%s is running'%name)
#     time.sleep(2)
#     print('%s is done'%name)
#
# if __name__ == '__main__':
#     t = Thread(target = task,args = ('子线程1',))
#     t.daemon = True
#     t.start()
#
#     print('主线程')


import time
from threading import Thread

def task(name):
    time.sleep(1)
    print('%s id running'%name)

def foo(name):
    print('%s is running'%name)
    time.sleep(3)
    print('%s is done'%name)

if __name__ == '__main__':
    t1 = Thread(target = task,args = ('task子线程',))
    t2 = Thread(target = foo,args = ('foo子线程',))

    t1.daemon = True
    t1.start()
    t2.start()

    print('主线程')
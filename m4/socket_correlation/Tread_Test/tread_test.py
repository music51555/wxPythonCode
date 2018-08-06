import time

from threading import Thread,current_thread,enumerate

def task():
    print('子线程的名字是%s'%current_thread().getName())
    time.sleep(2)

if __name__ == '__main__':
    t = Thread(target = task)
    t.setName('子进程1')
    t.start()
    print(enumerate())
    print('主线程')

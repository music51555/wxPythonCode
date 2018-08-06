# from threading import Thread
# import time
#
# def task(name):
#     print('%s is running'%name)
#     time.sleep(2)
#     print('%s is done'%name)
#
# if __name__ == '__main__':
#     t = Thread(target = task,args = ('子线程',))
#     t.start()

from threading import Thread,current_thread,active_count,enumerate
import time

class MyThread(Thread):

    def run(self):
        print('%s is running'%current_thread().getName())
        time.sleep(2)
        print('%s is done'%current_thread().getName())

if __name__ == '__main__':
    m = MyThread()
    m.setName('子线程')
    print(m.is_alive())
    m.start()
    print(m.is_alive())
    print(active_count())
    print(enumerate())

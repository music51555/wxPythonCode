#8、请写一个包含10个线程的程序，主线程必须等待每一个子线程执行完成之后才结束执行，
# 每一个子线程执行的时候都需要打印当前线程名、当前活跃线程数量。

from threading import Thread,current_thread,active_count

def task():
    print('current thread name is %s,active_count is %s'%(current_thread().getName,
                                                          active_count()))

if __name__ == '__main__':
    t_l = []
    for i in range(10):
        t = Thread(target=task,name='子线程%s'%i)
        t.start()
        t_l.append(t)

    for t in t_l:
        t.join()

    print('主')


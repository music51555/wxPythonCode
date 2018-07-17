from threading import Thread,current_thread,active_count,enumerate

def task():
    print('%s is running'%current_thread().getName())
    print(current_thread().is_alive())
    print(active_count())
    print(enumerate())

if __name__ == '__main__':
    t = Thread(target = task,name = '子线程2')
    t.setName('子线程1')
    print(t.is_alive())
    t.start()

    print('主线程')
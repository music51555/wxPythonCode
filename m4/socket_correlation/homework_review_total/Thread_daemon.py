from threading import Thread,current_thread
import time

def task():
    print('%s is running'%current_thread().getName())
    time.sleep(2)
    print('%s is done'%current_thread().getName())

if __name__ == '__main__':
    t = Thread(target = task)
    t.daemon = True
    t.start()

    print('主')
from threading import Thread,Event,current_thread
import time

def task(event):
    print('%s is running'%current_thread().getName())
    time.sleep(5)
    event.set()

def done(event):
    count = 0
    while not event.is_set():
        time.sleep(1)
        print('%s'%count)
        count += 1
    print('%s is done'%current_thread().getName())

if __name__ == '__main__':
    event = Event()
    t1 = Thread(target = task,args = (event,))
    t2 = Thread(target = done,args = (event,))

    t1.start()
    t2.start()
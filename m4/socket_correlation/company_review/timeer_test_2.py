from threading import Timer,current_thread

def task():
    print('%s is running'%current_thread().getName())
    t = Timer(interval = 5,function = task)
    t.start()

if __name__ == '__main__':
    task()
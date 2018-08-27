from multiprocessing import Process

n = 100

def task():
    global n
    n = 0
    print('子进程内n=%s'%n)

if __name__ == '__main__':
    p = Process(target=task)
    p.start()

    print('主进程内n=%s'%n)
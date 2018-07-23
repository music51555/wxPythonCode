import queue

def task(q):
    q.put('first')
    q.put('second')
    q.put('third')

def foo(q):
    print(q.get())
    print(q.get())
    print(q.get())

if __name__ == '__main__':
    q = queue.Queue()
    task(q)
    foo(q)

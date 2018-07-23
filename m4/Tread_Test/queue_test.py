import queue

def task(q):
    q.put((1,'first'))
    print('put first')
    q.put((3,'second'))
    print('put second')
    q.put((2,'third'))
    print('put third')
    print(q.qsize())

def foo(q):
    print(q.get())
    print(q.get())
    print(q.get())

if __name__ == '__main__':
    q = queue.PriorityQueue(3)
    task(q)
    foo(q)
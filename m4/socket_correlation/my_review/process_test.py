# from multiprocessing import Queue
#
# q = Queue(3)
#
# q.put(1)
# q.put([1,2,3,4])
# q.put('hello world')
# print(q.full())
#
# print(q.get())
# print(q.get())
# print(q.get())
# print(q.empty())


from multiprocessing import Process,Queue

def task(q):
    q.put(1)
    print('put')
    q.put(2)
    print('put')
    q.put(3)
    print('put')

def foo(q):
    print(q.get())
    print(q.get())
    print(q.get())

if __name__ == '__main__':
    q = Queue(2)
    p1 = Process(target=task,args=(q,))
    p1.start()

    p2 = Process(target=foo,args=(q,))
    p2.start()
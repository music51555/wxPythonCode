import queue

q = queue.PriorityQueue(3)
q.put((10,'first'))
q.put((30,'twice'))
q.put((20,'third'))

print(q.get())
print(q.get())
print(q.get())
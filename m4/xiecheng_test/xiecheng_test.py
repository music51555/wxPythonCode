# import time
#
# def product():
#     data_list = []
#     for i in range(10000000):
#         data_list.append(i)
#     return data_list
#
# def customer(data_list):
#     print(data_list)
#
# start_time = time.time()
# res = product()
# customer(res)
# end_time = time.time()
# #3.286834955215454秒
# print(end_time - start_time)

import time

def product():
    g = customer()
    next(g)
    for i in range(10000000):
        g.send(i)

def customer():
    while True:
        x = yield

start_time = time.time()
product()
end_time = time.time()
#1.4196021556854248秒
print(end_time - start_time)
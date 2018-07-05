import time

def set_time(*args):
    if not args:
        time_stamp = time.localtime(time.time())
        current_time = time.strftime('%Y-%m-%d %H:%M:%S',time_stamp)
        return current_time
    else:
        print(args)
        current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(args[0]))
        print(current_time)
        return current_time
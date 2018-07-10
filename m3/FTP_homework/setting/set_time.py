import time

def set_time(*args):
    if not args:
        time_stamp = time.localtime(time.time())
        current_time = time.strftime('%Y-%m-%d %H:%M:%S',time_stamp)
        return current_time
    else:
        current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(args[0]))
        return current_time
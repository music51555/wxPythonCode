import sys
import time

def set_bar():
    count = 0
    while count < 6:
        sys.stdout.write('=>')
        sys.stdout.flush()
        time.sleep(0.2)
        count += 1
        if count == 5:
            sys.stdout.write('\r')
            sys.stdout.write('          ')
            sys.stdout.write('\r')
            count = 0
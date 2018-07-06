import sys
import time

def set_bar():
    count = 0
    while count < 20:
        sys.stdout.write('=>')
        sys.stdout.flush()
        time.sleep(0.1)
        count += 1
    sys.stdout.write('\n')

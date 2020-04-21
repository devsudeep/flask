import sys
import time
import threading


def print_func(msg):
    for i in range(10):
        status = str(i) + ' ' + msg
        sys.stdout.write(str(i) + msg)
        sys.stdout.flush()
        sys.stdout.write('\x08' * len(status))
        time.sleep(1)

# print_func('sudeep')

spinner = threading.Thread(target=print_func, args=('Hello!',))
print('spriner object:',spinner)
spinner.start()
time.sleep(10)
spinner.join()

import threading
import itertools
import time
import sys
import asyncio


class Signal:
    go = True

@asyncio.coroutine
def spin(msg):
    write, flush = sys.stdout.write, sys.stdout.flush
    for char in itertools.cycle('|/-\\'):
        print("running async process.")
        status = char + ' ' + msg
        write(status)
        flush()
        write('\x08' * len(status))
        try:
            yield from asyncio.sleep(10)

        except asyncio.CancelledError:
            break

    write(' ' * len(status) + '\x08' * len(status))

@asyncio.coroutine
def slow_function():
    # pretend waiting a long time for I/O
    yield from asyncio.sleep(100)
    return 42

@asyncio.coroutine
def supervisor():
    spinner = asyncio.async(spin('thinking!'))
    print('spinner object:', spinner)
    for i in range(10):
        print(i)
        time.sleep(1)
    result = yield from slow_function()
    spinner.cancel()
    return result


def main():
    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(supervisor())
    loop.close()
    print('Answer:', result)


if __name__ == '__main__':
    main()
    for i in range(10):
        sys.stdout.write(str(i))
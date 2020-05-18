import asyncio
import sys


@asyncio.coroutine
def loop10000():
    for i in range(100):
        print(i)
        yield from asyncio.sleep(0.2)



@asyncio.coroutine
def loop10k():
    for i in range(10000):
        print(i)
        yield from asyncio.sleep(0.2)



loop = asyncio.get_event_loop()
looper = asyncio.async(loop10000())

loop.close()

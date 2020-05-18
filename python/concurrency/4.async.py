import sys
import time
from colorama import init
from colorama import Fore, Back, Style
import asyncio

sys.set_coroutine_wrapper(lambda x: 42)

init()


async def foo():
    time.sleep(100)
    print("running async process")
    pass


foo()
print("Starting sync process")


# async def asy1():
#     for i in range(100):
#         print(Fore.RED + + '------------' + str(i))


# async def asy2():
#     for i in range(100):
#         print(Fore.GREEN + + '------------' + str(i))


# async def asy3():
#     for i in range(100):
#         print(Fore.BLUE + + '------------' + str(i))

# asyncio.gather(asy1, asy2, asy3)

# loop = asyncio.get_event_loop()
# loop.run_until_complete()

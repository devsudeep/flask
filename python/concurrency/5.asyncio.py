import asyncio
import sys
import time

async def main():
    print("main")
    # await asyncio.sleep(1)
    print(".........hello")
    for i in range(10):
        sys.stdout.write(str(i))
        time.sleep(1)
    sys.stdout.flush()

def hello():
    for i in range(10):
        print(i)

asyncio.run(main())
hello()


def contatebate(a, b):
    return a + b

contatebate("sudeep", "patel")


print(contatebate.__code__)
import dis

print(dis.dis(contatebate))
print(dis.dis(hello))

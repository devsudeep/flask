import asyncio


async def count():
    print('one')
    await asyncio.sleep(1)
    print('two')


async def lopper1():
    for i in range(100):
        print(i)
        await asyncio.sleep(1)


async def lopper2():
    for i in range(100):
        print(i)
        await asyncio.sleep(0.1)


async def lopper3():
    for i in range(100):
        print(i)
        # await asyncio.sleep(0.1)
        await lop()


async def lop():
    for i in range(1000):
        pass


async def main():
    await asyncio.gather(count(), count(), count(), lopper1(), lopper2(), lopper3())

if __name__ == '__main__':
    import time
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")

    async def f(x):
        y = await z(x)  # OK - `await` and `return` allowed in coroutines
        return y

    async def g(x):
        yield x  # OK - this is an async generator

    # async def m(x):
    #     yield from gen(x)  # No - SyntaxError

    # def m(x):
    #     y = await z(x)  # Still no - SyntaxError (no `async def` here)
    #     return y

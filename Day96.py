# AsyncIO in Python

import time
import asyncio


async def function1():
    # time.sleep(3)
    asyncio.sleep(1)
    print("Func 1")
    return "Udoy"


async def function2():
    # time.sleep(3)
    asyncio.sleep(1)
    print("Func 2")


async def function3():
    # time.sleep(3)
    asyncio.sleep(4)
    print("Func 3")


async def main():
    # task = asyncio.create_task(function1())
    # # await function1()
    # await function2()
    # await function3()

    L = await asyncio.gather(
        function1(),
        function2(),
        function3(),
    )

    print(L)


asyncio.run(main())

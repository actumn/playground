# codes from https://tutorialedge.net/python/concurrency/asyncio-tasks-tutorial/
import asyncio
import time


async def my_task(id):
    time.sleep(1)
    print(f'{id} Processing task')

    for task in asyncio.Task.all_tasks():
        print(task)
        task.cancel()
        print(task)


# One of the key things to note about tasks in Asyncio is that
# you don’t directly create them, you instead use the ensure_future() function or the AbstractEventLoop.create_task()
async def my_task_generator():
    for i in range(5):
        asyncio.ensure_future(my_task(i))

    # pending = asyncio.Task.all_tasks()
    # print(pending)
"""
loop = asyncio.get_event_loop()
loop.run_until_complete(my_task_generator())
print('Completed all tasks')
loop.close()
"""


async def my_worker_task(number):
    return number * 2


async def main_task(coros):
    for fs in asyncio.as_completed(coros):
        print(await fs)

"""
try:
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main_task([my_worker_task(i) for i in range(5)]))
except KeyboardInterrupt:
    pass
finally:
    loop.close()
"""


async def my_worker():
    print('Hello world')


async def main():
    print('My main')


try:
    loop = asyncio.get_event_loop()
    # loop.run_until_complete(asyncio.gather(*[my_worker() for _ in range(5)]))
    loop.run_until_complete(asyncio.wait([my_worker() for _ in range(5)], timeout=2))
except KeyboardInterrupt:
    pass
finally:
    loop.close()

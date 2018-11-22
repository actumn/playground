# codes from https://tutorialedge.net/python/concurrency/python-asyncio-semaphores-tutorial/
import asyncio
import time


async def my_worker(semaphore):
    await semaphore.acquire()
    print('successfully acquired the semaphore')
    await asyncio.sleep(3)
    print('Releasing Semaphore')
    semaphore.release()

async def main(loop):
    my_semaphore = asyncio.Semaphore(value=2)
    await asyncio.wait([my_worker(my_semaphore), my_worker(my_semaphore), my_worker(my_semaphore)])
    print('Main coroutine')

loop = asyncio.get_event_loop()
loop.run_until_complete(main(loop))
print('All workers completed')
loop.close()

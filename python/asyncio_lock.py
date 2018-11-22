# codes from https://tutorialedge.net/python/concurrency/asyncio-synchronization-primitives-tutorial/
import asyncio
import time


async def my_worker(lock):
    print('Attempting to attain lock')

    with await lock:
        print('currently locked')
        time.sleep(2)

    print('Unlocked Critical Section')


async def main():
    lock = asyncio.Lock()
    await asyncio.wait([my_worker(lock), my_worker(lock)])


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
print('All tasks completed')
loop.close()


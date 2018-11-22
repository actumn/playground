# codes from https://tutorialedge.net/python/concurrency/asyncio-synchronization-primitives-tutorial/
import asyncio
import random
import time


async def news_producer(my_queue):
    while True:
        await asyncio.sleep(1)
        print('Putting news item onto queue')
        await my_queue.put(random.randint(1, 5))


async def news_consumer(id, my_queue):
    print(my_queue)
    while True:
        print(f'Consumer: {id} Attempting to get to get from queue')
        item = await my_queue.get()
        if item is None:
            break

        print(f'Consumer: {id} consumed article with id: {item}')

loop = asyncio.get_event_loop()
my_queue = asyncio.Queue(loop=loop, maxsize=10)
try:
    loop.run_until_complete(asyncio.gather(news_producer(my_queue),
                                           news_consumer(1, my_queue),
                                           news_consumer(2, my_queue)))
except KeyboardInterrupt:
    pass
finally:
    loop.close()

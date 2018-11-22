import asyncio
import datetime
import random
import types


# Generator
@asyncio.coroutine
def display_date(num, loop):
    end_time = loop.time() + 50.0
    while True:
        print(f'Loop: {num} Time: {datetime.datetime.now()}')
        if (loop.time() + 1.0) >= end_time:
            break

        yield from asyncio.sleep(random.randint(0, 5))


@types.coroutine
def my_sleep_func():
    yield from asyncio.sleep(random.randint(0, 5))


# Native coroutine (after python 3.5): Like above
# There’s no functional differences, and we can interoperate between those
async def display_date_new(num, loop):
    end_time = loop.time() + 50.0
    while True:
        print(f'Loop: {num} Time: {datetime.datetime.now()}')
        if (loop.time() + 1.0) >= end_time:
            break

        await my_sleep_func()


loop = asyncio.get_event_loop()
# We use asyncio.ensure_future() to schedule the execution of the coroutine in the default event loop
# Two coroutines run concurrently (but not in parallel since the event loop is single threaded).
asyncio.ensure_future(display_date_new(1, loop))
asyncio.ensure_future(display_date_new(2, loop))

loop.run_until_complete(display_date(4, loop))
# loop.run_forever()

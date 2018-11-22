# codes from https://tutorialedge.net/python/concurrency/getting-started-with-asyncio-python/
# ensure_future vs create_task vs simple coroutine:
#   https://stackoverflow.com/questions/36342899/asyncio-ensure-future-vs-baseeventloop-create-task-vs-simple-coroutine
import asyncio
import random


# Define a coroutine that takes in a future
async def my_coroutine_future(future):
    # simulate some 'work'
    await asyncio.sleep(1)
    # set the result of our future object
    future.set_result('My Coroutine-turned-future has completed')


async def main_future():
    # define a future object
    future = asyncio.Future()
    # wait for the completion of our coroutine that we've
    # turned into a future object using the ensure_future() function
    await asyncio.ensure_future(my_coroutine_future(future))
    # await my_coroutine(future)

    # Print the result of our future
    print(future.result())


async def my_coroutine(id):
    process_time = random.randint(1, 5)
    await asyncio.sleep(process_time)
    print(f'Coroutine: {id}, has successfully completed after {process_time} seconds')


async def main():
    tasks = []
    for i in range(10):
        tasks += [asyncio.ensure_future(my_coroutine(i))]

    await asyncio.gather(*tasks)


loop = asyncio.get_event_loop()
try:
    loop.run_until_complete(main())
finally:
    loop.close()

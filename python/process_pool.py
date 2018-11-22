# codes from https://tutorialedge.net/python/concurrency/python-processpoolexecutor-tutorial/
from concurrent.futures import ProcessPoolExecutor
import os


def task():
    print(f'Executing our task on process: {os.getpid()}')


def main():
    with ProcessPoolExecutor(max_workers=3) as executor:
        task1 = executor.submit(task)
        task2 = executor.submit(task)


if __name__ == '__main__':
    main()

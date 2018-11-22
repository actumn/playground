# codes from http://masnun.com/2015/11/13/python-generators-coroutines-native-coroutines-and-async-await.html
def simple_gen():
    yield 'Hello'
    yield 'World'



def generate_nums():
    num = 0
    while True:
        yield num
        num = num + 1


def coro():
    hello = yield 'Hello'
    yield hello


if __name__ == '__main__':
    # a generator function doesn’t directly return any values
    # but when we call it, we get a generator object which is like an iterable
    # So we can call next() on a generator object to iterate over the values. Or run a for loop.
    gen = simple_gen()
    print(gen)
    print(next(gen))
    print(next(gen))
    # print(next(gen))  # here will be error

    """
    for x in generate_nums():
        print(x)
        if x > 9:
            break
    """
    # What if we wanted to push some data too?
    c = coro()
    print(next(c))
    print(c.send('World'))

# codes from https://gist.github.com/jcfrank/9c2f3b4d4bd2d6ec44b7

def simple_decorator(func):
    print('This function is decorated with a decorator with no argument.')
    def actual(*args, **kwargs):
        return func(*args, **kwargs)
    return actual

"""
Followings are the same as:

def simple_print(message):
    print(f'Hello {message}')

simple_decorator(simple_print)('simple decorator!')
"""

@simple_decorator
def simple_print(message):
    print(f'Hello {message}')
  

simple_print('simple decorator!')

print("\n========\n")

def decorator_with_args(arg1, arg2):
    def inner_decorator(func):
        print('This function is decorated with a decorator with no argument.')
        def actual(*args, **kwargs):
            return func(*args, **kwargs)
        return actual

    return inner_decorator

"""
followings are the same as:
def print_again(message):
    print(f'Hello {message}')

decorator_with_args(arg1, arg2)(print_again)('decorator with arguments!')
"""
@decorator_with_args('a1', 'a2')
def print_again(message):
    print(f'Hello {message}')

print_again('decorator with arguments!')

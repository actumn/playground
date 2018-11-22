# codes from https://dojang.io/mod/page/view.php?id=1047
def print_numbers(a, b, c):
    print(a, b, c)


def print_numbers_args(*args):
    print(*args)


def print_numbers_mix(a, *args):
    print(a, args)
    print(a, *args)


x = [10, 20, 30]
print_numbers(*x)
print_numbers(*[10, 20, 30])
# print_numbers(*[10, 20, 30, 40])  # here will be error

print_numbers_args(*[10, 20, 30])
print_numbers_args(*[10, 20, 30, 40])

print_numbers_mix(*[10, 20, 30])
print_numbers_mix(*[10, 20, 30, 40])


def personal_info(name, age, address):
    print(f'이름: {name}, 나이: {age}, 주소: {address}')


def personal_info_kwargs(**kwargs):
    for kw, arg in kwargs.items():
        print(f'{kw}: {arg}', sep='')


x = {'name': '홍길동', 'age': 30, 'address': '서울시 용산구 이촌동'}
personal_info(**x)
personal_info(**{'name': '홍길동', 'age': 30, 'address': '서울시 용산구 이촌동'})

personal_info_kwargs(name='홍길동')
personal_info_kwargs(name='홍길동', age=30, address='서울시 용산구 이촌동')


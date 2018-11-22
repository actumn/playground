# cods from https://tutorialedge.net/python/python-method-resolution-order-tutorial/
class AwesomeClass:

    def __init__(self):
        print('My Awesome Class')

    def test_func(self):
        print('This is my awesome class')


class NotAwesomeClass:

    def __init__(self):
        print('My Not Awesome Class')

    def test_func(self):
        print('This is not my awesome class')


# class MySuperClass(NotAwesomeClass, AwesomeClass):
class MySuperClass(AwesomeClass, NotAwesomeClass):

    def __init__(self):
        super().__init__()
        print('My Super Class')


my_class = MySuperClass()
my_class.test_func()

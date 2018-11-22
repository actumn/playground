# codes from https://www.tutorialspoint.com/python/python_classes_objects.htm
class Employee:
    """
    Common base
    """
    emp_count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.emp_count += 1

    @staticmethod
    def display_count():
        print('Total Employee %d' % Employee.emp_count)

    def display_employee(self):
        print(self.__str__())

    def __str__(self):
        return f'Name: {self.name}, Salary: {self.salary}'


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __del__(self):
        class_name = self.__class__.__name__
        print(class_name, 'destroyed')


class Parent:
    parent_attr = 100

    def __init__(self):
        print('Calling parent constructor')

    @staticmethod
    def parent_method():
        print('Calling parent method')

    @staticmethod
    def set_attr(attr):
        Parent.parent_attr = attr

    @staticmethod
    def get_attr():
        print('Parent attribute: ', Parent.parent_attr)

    @staticmethod
    def my_method():
        print('Calling parent my_method')


class Child(Parent):

    def __init__(self):
        super().__init__()
        print('Calling child constructor')

    @staticmethod
    def child_method():
        print('Calling child method')

    @staticmethod
    def my_method():
        print('Calling child my_method')


class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return f'Vector ({self.a}, {self.b})'

    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)


class JustCounter:
    __secret_count = 0

    def count(self):
        self.__secret_count += 1
        print(self.__secret_count)


if __name__ == '__main__':
    emp1 = Employee('Zara', 2000)
    emp2 = Employee('Mann1', 5000)

    emp1.display_employee()
    emp2.display_employee()
    print(f'Total Employee {Employee.emp_count}')
    print(f'emp1 count {emp1.emp_count}')

    emp1.age = 7
    emp1.age = 8
    print(hasattr(emp1, 'age'))
    print(emp1.age)
    delattr(emp1, 'age')

    print(hasattr(emp1, 'age'))

    print('Employee.__doc__:', Employee.__doc__)
    print('Employee.__name__:', Employee.__name__)
    print('Employee.__module__:', Employee.__module__)
    print('Employee.__bases__:', Employee.__bases__)
    print('Employee.__dict__:', Employee.__dict__)

    pt1 = Point()
    pt2 = pt1
    pt3 = pt1
    print(id(pt1), id(pt2), id(pt3))
    del pt1
    del pt2

    c = Child()
    c.child_method()
    c.parent_method()
    c.set_attr(200)
    c.get_attr()
    c.my_method()

    v1 = Vector(2, 10)
    v2 = Vector(5, -2)
    print(v1 + v2)

    counter = JustCounter()
    counter.count()
    counter.count()
    # print(counter.__secret_count)  # <-- here will be error
    print(counter._JustCounter__secret_count)

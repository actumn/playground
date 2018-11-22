# codes from http://bluese05.tistory.com/30
import datetime


class DatetimeDecorator:
    def __init__(self, f):
        self.func = f

    def __call__(self, *args, **kwargs):
        print(datetime.datetime.now())
        self.func(*args, **kwargs)
        print(datetime.datetime.now())


@DatetimeDecorator
def main_function():
    print('Main Function')


class Something:

    @staticmethod
    @DatetimeDecorator
    def main_function():
        print('Main Function')


class WeatherSimulation:

    def __init__(self, **params):
        self.params = params

    @classmethod
    def for_winter(cls, **other_params):
        params = {'month': 'Jan', 'temp': '0'}

        params.update(other_params)

        return cls(**params)

    @property
    def progress(self):
        return self.completed_iterations / self.total_iterations

    @property
    def completed_iterations(self):
        return 10

    @property
    def total_iterations(self):
        return 20


if __name__ == '__main__':
    some = Something()
    some.main_function()
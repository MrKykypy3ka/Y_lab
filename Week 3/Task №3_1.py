import random


def cache_decorator(func):
    double_numbers = dict()

    def wrapper(number):
        nonlocal double_numbers
        if number not in double_numbers:
            double_numbers[number] = func(number)
        print(f'Кэш: {double_numbers}')
        return double_numbers[number]
    return wrapper


@cache_decorator
def multiplier(number: int):
    return number * 2


if __name__ == "__main__":
    for _ in range(10):
        print(multiplier(random.randint(1, 30)))


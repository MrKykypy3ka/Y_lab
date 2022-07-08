import random


double_numbers = dict()


def decorator(func):
    def wrapper(number):
        if number not in double_numbers:
            double_numbers[number] = func(number)
        return double_numbers[number]
    return wrapper


@decorator
def multiplier(number: int):
    return number * 2


if __name__ == "__main__":
    for _ in range(5):
        print(multiplier(random.randint(1, 30)))

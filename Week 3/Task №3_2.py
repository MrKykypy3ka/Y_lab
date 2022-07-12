import time


def wait_decorator(call_count, start_sleep_time, factor, border_sleep_time):
    def decorator(func):
        def wrapper(*args, **kwargs):
            t = start_sleep_time
            print(f'Кол-во запусков = {call_count}')
            print('Начало работы')
            for i in range(call_count):
                func_result = func(*args, **kwargs)
                if t < border_sleep_time:
                    t = start_sleep_time * factor ** i
                else:
                    t = border_sleep_time
                print(f'Запуск номер {i + 1}. Ожидание: {t} секунд. Результат декорируемой функций = {func_result}.')
                time.sleep(t)

            print('Конец работы')
            return
        return wrapper
    return decorator


@wait_decorator(call_count=4, start_sleep_time=1, factor=2, border_sleep_time=10)
def multiplier(number: int):
    return number * 2


def main():
    multiplier(2)


if __name__ == "__main__":
    main()
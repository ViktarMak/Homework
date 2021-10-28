# Task 4.6
# Implement a decorator call_once which runs a function or method once and caches the result.
# All consecutive calls to this function should return cached result no matter the arguments.


def call_once(func):

    cash = 0

    def wrapper(*args):
        nonlocal cash
        if cash == 0:
            cash = func(*args)
            return cash
        else:
            return cash

    return wrapper


@call_once
def sum_of_num(a, b):
    return a + b


if __name__ == '__main__':
    print(sum_of_num(13, 42))
    print(sum_of_num(999, 100))
    print(sum_of_num(134, 412))
    print(sum_of_num(856, 232))

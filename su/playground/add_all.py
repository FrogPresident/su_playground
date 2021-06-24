def add_all(*numbers):
    sum_ = 0
    for number in numbers:
        sum_ += number
    return sum_


def show_values(**kwargs):
    for key, val in kwargs.items():
        print(f'{key}={val}')

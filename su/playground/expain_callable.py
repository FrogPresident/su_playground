from typing import Callable


def main():
    func = MyFunc(1)
    func2 = MyFunc(2)

    print(func(4))
    print(func2(5))
    print(isinstance(func, Callable))


class MyFunc:
    def __init__(self, i):
        print("init")
        self.i = i

    def __call__(self, j):
        print("calling", j)
        return self.i + j


if __name__ == '__main__':
    main()

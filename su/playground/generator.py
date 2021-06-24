from typing import Iterator, Iterable


def main():
    gen = my_generator(0, 10)
    for i in gen:
        print(i)
    print(type(gen))
    assert isinstance(gen, Iterator)
    assert isinstance(gen, Iterable)


def my_generator(start, end):
    k = start
    while k <= end:
        yield k
        k += 1


if __name__ == '__main__':
    main()

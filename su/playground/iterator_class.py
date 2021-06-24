from typing import Iterator, Iterable


def main():
    it = MyIter(0, 10)
    for i in it:
        print(i)
    assert isinstance(it, Iterable)
    assert isinstance(it, Iterator)
    assert iter(it) is it


class MyIter(Iterator):
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.current = start

    def __next__(self):
        current = self.current
        if current > self.end:
            raise StopIteration()
        self.current += 1
        return current


if __name__ == '__main__':
    main()

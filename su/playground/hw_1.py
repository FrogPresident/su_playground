from typing import Iterator


def main():
    ans = get_ans(map)
    print(ans)
    print(ans == get_ans(mymap))
    print(ans == get_ans(MapIter))


def mymap(func, *iterables):
    for args in zip(*iterables):
        yield func(*args)


class MapIter(Iterator):
    def __init__(self, func, *iterables):
        self.func = func
        self.iter = zip(*iterables)

    def __next__(self):
        return self.func(*next(self.iter))


def get_ans(iter_):
    return ','.join(iter_(lambda x, y: x * 2 + y * 3, "abcz", "def"))


if __name__ == '__main__':
    main()

def main():
    li = [1, 4, 5, 6, 3, 21, 7, 4, 2, 5, 8]
    li2 = [12, 42, 52, 62, 32, 212, 72, 42, 22, 52]
    li3 = [121, 421, 521, 612, 312, 2112, 172, 412, 212, 512]
    for element in li:
        print(element, end=" ")
    print()

    for i, element in enumerate(li):
        print(f'{i}:{element}', end=" ")
    print()

    for i, element in enum(li):
        print(f'{i}:{element}', end=" ")
    print()

    for e1, e2 in zip(li, li2):
        print(f'({e1},{e2})', end=" ")
    print()

    for e1, e2, e3 in my_zip(li, li2, li3):
        print(f'({e1},{e2},{e3})', end=" ")
    print()

    for i in map(lambda x: x * 2, [i for i in range(10)]):
        print(i, end=" ")


def my_zip(*iterables):
    iterators = []
    for iterable in iterables:
        iterators.append(iter(iterable))

    while True:
        elements = []
        for iterator in iterators:
            try:
                elements.append(next(iterator))
            except StopIteration:
                return
        yield tuple(elements)


def enum(iter_, start=0):
    k = start
    for i in iter_:
        yield k, i
        k += 1


if __name__ == '__main__':
    main()

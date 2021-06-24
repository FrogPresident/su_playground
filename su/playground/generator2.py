def generator(start, end):
    k = start
    if k <= end:
        yield k
    k += 1


def main():
    gen = generator(0, 10)
    for i in gen:
        print(i)


if __name__ == '__main__':
    main()

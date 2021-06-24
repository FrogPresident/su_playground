def main():
    li = [1, 5, 2, 3]
    t = (1, 3, 5)
    di = {
        "a": 1,
        "b": 2
    }

    it = iter(di.items())

    def inner(t):
        k,v = t
        print(k,v)

    try:
        while True:
            inner(next(it))
    except StopIteration:
        pass

    # for k, v in di.items():
    #     print(k, v)


if __name__ == '__main__':
    main()

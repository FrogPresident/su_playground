def main():
    """
    *
    """
    func(1, 2, 3, a="4", b="5", c="6")  #

    li = ["a", "b", "c"]
    di = {"t": 1, "y": 2, "z": 3}
    y = 4
    # a b c 1 4 2 3
    explicit_func(*li, x=y, **di)

    lia = [1, 2]
    lib = [4, 5]
    # [1, 2, 3, 4, 5]
    li = lia + [3] + lib
    print(li)
    li = [*lia, 3, *lib]
    print(li)

    dia = {"a": 3, "b": 8}
    dib = {"c": 7, "d": 10}
    x = 9
    dic = {**dia, "j": x, **dib}
    print(dic)


def func(x, *args, **kwargs):
    print(x)
    print(args)  # list all positional arguments as a tuple
    print(kwargs)  # list all keyword arguments as a dict


def explicit_func(a, b, c, t, x, y, z):
    print(a, b, c, t, x, y, z)


if __name__ == '__main__':
    main()

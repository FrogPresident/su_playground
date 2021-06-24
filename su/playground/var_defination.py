def main():
    a = 'abc'
    b = 5
    c = 5.13
    d = True
    e = b'abc'
    f = 1 + 5j

    print(type(a))
    print(type(b))
    print(type(c))
    print(type(d))
    print(type(e))
    print(type(f))

    # -----str-----
    s1 = "abc"
    s2 = 'abc'
    s3 = f'abc{123:010d}{{}}'
    s4 = "abc%.2f, %d" % (1.23, 123)
    s5 = "abc{:2d}".format(123)
    s6 = "abc{id:2d}".format(id=123)
    print(s3, s4, s5, s6, sep="\n")

    # -----float------
    f1 = 123.456
    f2 = 123.
    f3 = .456
    f4 = 1.456E3


if __name__ == '__main__':
    main()

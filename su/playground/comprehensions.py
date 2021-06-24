def main():
    # print([
    #     c * i
    #     for i in range(1, 3)
    #     for c in "abc"
    # ])
    # print(*[
    #     c * i
    #     for i in range(1, 6)
    #     for c in "abcde"
    #     if ord(c) - ord("a") != i
    # ])
    # print({
    #     a: a * b
    #     for a in range(1, 5)
    #     for b in '12345'
    #     if ord(b) - ord('1') != b
    # })

    di = {}
    for a in range(1, 5):
        for b in '1234567':
            if ord(b) - ord('1') != a:
                di[(a, b)] = a * b
    print(di)


if __name__ == '__main__':
    main()

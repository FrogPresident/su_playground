def main():
    li = [1, 2, 3]
    print([2, 3] * 5)
    li.append(1)
    print(li)
    li.pop()
    print(li)
    print([2, 2, 3, 3, 4, 3].count(4))
    print([2, 2, 3, 3, 4, 3].index(4))
    print([2, 2, 3, 3, 4, 3][2])
    print([2, 2, 3, 3, 4, 3][2:4])
    print([2, 2, 3, 3, 4, 3][slice(2, 4)])

    li[0:2] = [8, 9]
    print(li[:] is li, li[:] == li)
    print(li)

    t = (1, 2, 3)  # immutable
    print(t[0:1])

    dic = {
        "key": "val",
        "ke2y": "val2"
    }
    print(dic)
    print(dic.keys())
    print(dic.values())
    print(list(dic))
    print(list(dic.items()))

    se = {1, 2, 3}
    print(type(se))
    print(type({}))
    print(type(set()))
    print(se - {2})
    se.add(1)
    print(se)
    print(se.intersection({1, 3, 4, 5}))
    print(se.union({1, 2, 4, 5}))
    li2 = [1, 2, 2, 3, 3, 4, 5, 6]
    print(list(set(li2)))


if __name__ == '__main__':
    main()

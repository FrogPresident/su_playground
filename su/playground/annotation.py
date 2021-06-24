outside: str
outside = 2.56
a: str


def main(param: bool, param2: int) -> list[str]:
    local_var: str
    print(outside)
    print(__annotations__)
    print(main.__annotations__)
    print(A.__annotations__)
    print(A.a.__annotations__)
    print(A.b.__annotations__)
    return ["2", "1"]


class A:
    class_var: str

    def a(self, i: int) -> bool:
        a_var: str
    def b(self, j: str, k: bool) -> "A": ...  # forward reference(還沒定義，之後會定義)


if __name__ == '__main__':
    main(True, 1)


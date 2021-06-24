def main():
    print(add_to(3))

CONST_B = 6
def add_to(n):
    count = 0
    for i in range(1, n + 1):
        count += i
    return count


if __name__ == '__main__':
    main()

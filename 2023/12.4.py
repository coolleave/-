def test1():
    for i in range(3):
        for s in "abcd":
            if s == 'c':
                break
            print(s, end="")


def test2():
    s1 = {1, 3, 5}
    s2 = {4, 5, 6}
    print(s1 | s2)

def test3():
    a = 123
    b = 456
    print(a and b)
    print(a or b)


if __name__ == '__main__':
    test3()
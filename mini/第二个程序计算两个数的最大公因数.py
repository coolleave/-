while True:
    a = int(input("请输入第一个数字"))
    b = int(input("请再输入一个数字"))

    while True:
        if a > b:
            a = a - b
        if b > a:
            b = b - a
        if a == b:
            print(f"他们的最大公约数为{a}")
            break


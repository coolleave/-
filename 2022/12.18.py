num = 0
for i in range(1, 10):
    if i == 6:
        pass
    else:
        for a in range(0, 10):
            if a == i or a == 6:
                pass
            else:
                for b in range(0, 10):
                    if b == a or b == i or b == 6:
                        pass
                    else:
                        num += 1
                        print(i*1000 + a*100 + b*10 + 6)
print(f'一共有{num}')

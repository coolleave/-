import time
time1 = time.time()
line = 1
while line < 20000:
    print(f"第{line}天")
    line += 1
if line >= 20000:
    print("已经完成")
time2 = time.time()
print(time2 - time1)

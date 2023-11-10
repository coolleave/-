# 文件复制
with open("壁纸.jpg", mode="rb") as f1, \
        open("venv/壁纸.jpg", mode="wb") as f2:
    print(f1)
    for line in f1:
        f2.write(line)

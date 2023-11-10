import os
import time
# 张->刘
with open("方圆几里", mode="r", encoding="utf-8") as f1,\
        open("方圆几里_副本", mode="w", encoding="utf-8") as f2:
    for line in f1:
        line.strip()  # 去除空格
        if line.startswith("张"):  # 判定是否以张开头
            line = line.replace("张", "刘")  # 替换张为刘
        f2.write(line)  # 写入f2文件
        # 今天就到这里 晚安！
time.sleep(3)
os.remove("方圆几里")
time.sleep(3)
os.rename("方圆几里_副本", "方圆几里")


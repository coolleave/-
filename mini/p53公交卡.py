v = int(input("获取当前公交卡余额"))
if v < 2:
    print("请投币")
elif v < 10:
    print("余额即将不足请及时充值")
    v = v-2
    print("乘车后余额"+str(v))
else:
    print("欢迎乘车！")
    v = v - 2
    print(f"乘车后余额{v}")

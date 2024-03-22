
# loss = (wx+b - y) ** 2 使得loss逐渐减少到0的点

# 传入参数，b，w 样本点集
def get_error(b, w, points):
    total_loss = 0
    for i in range(0, len(points)):
        x = points[i, 0]
        y = points[i, 1]
        # 累加总loss值
        total_loss += (w*x+b - y) ** 2

        # 返回平均loss值
    return total_loss/float(len(points))

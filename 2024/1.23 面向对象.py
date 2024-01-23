# 引子 模拟人狗大战
# 模板

# 攻击力字典储存
atrack_val_data = {
    '藏獒': 50,
    '二哈': 30,
    '茶杯': 15
}


# 输入狗的名称，类型，并计算攻击力
def dog(dg_name, type):
    atrack_val = 0
    # 匹配狗的攻击力
    for key, value in atrack_val_data:
        if type == key:
            atrack_val = value
    # 没找到狗的类型，默认攻击力为15
    if not atrack_val:
        atrack_val = 15

    data = {
        'name': dg_name,
        'type': type,
        'atrack_val': atrack_val,  # 攻击力
        'life_val': 100  # 生命值
    }
    return data


# 输入人的年龄并计算攻击力
def man(man_name, age):
    if age > 15:
        if age > 40:
            atrack_val = 50
        else:
            atrack_val = 70
    else:
        atrack_val = 30
    data = {
        'name': man_name,
        'atrack_val': atrack_val,
        'life_val': 100
    }
    return data


def man_atrack(dog_obj, man_obj):
    dog_obj['life_val'] -= man_obj['atrack_val']
    man_name = man_obj['name']
    dog_name = dog_obj['name']
    atrack_val = man_obj['atrack_val']
    life_val = dog_obj['life_val']
    print(f'【{man_name}】对【{dog_name}】发起攻击，造成了{atrack_val}, 剩余{life_val}点血量')


def dog_atrack(dog_obj, man_obj):
    man_obj['life_val'] -= dog_obj['atrack_val']
    man_name = man_obj['name']
    dog_name = dog_obj['name']
    atrack_val = dog_obj['atrack_val']
    life_val = man_obj['life_val']
    print(f'【{dog_name}】对【{man_name}】发起攻击，造成了{atrack_val}, 剩余{life_val}点血量')
# 封装


p1 = man('小明', 22)
p2 = dog('旺财', '藏獒')
if __name__ == '__main__':
    dog_atrack(p2, p1)
    man_atrack(p2, p1)
    dog_atrack(p2, p1)

import random
ques = [
    '模拟夜间行驶', '路边临时停车', '进入无照明的道路上行驶', '进入照明不良的道路上行驶',
    '会车', '同方向近距离跟车', '在照明良好的道路上行驶', '在有路灯的道路上行驶', '通过路口',
    '通过急弯', '通过拱桥',
    '通过坡路', '没有信号灯的路口', '人行横道', '超车', '结束夜间模拟'
]
keys = [
    '近光灯', '小灯双闪', '远光灯', '远近光灯交替', '关闭灯光'
]
print(f'一共有{len(ques)}个问题')
i = 0
while i < 15:
    que = ques[random.randint(0, len(ques)-1)]
    print(que)
    key = input('请输入答案\n')
    if que == ques[0] or que == ques[4]:
        if key == keys[0]:
            print('恭喜回答正确！！')
        else:
            print(f'回答错误，正确答案是{keys[0]}')
    elif que == ques[1]:
        if key == keys[1]:
            print('恭喜回答正确！')
        else:
            print(f'回答错误，正确答案是{keys[1]}')
    elif que == ques[2] or que == ques[3]:
        if key == keys[2]:
            print('恭喜回答正确')
        else:
            print(f'回答错误，正确答案是{keys[2]}')
    elif que == ques[-1]:
        if key == keys[-1]:
            print('恭喜回答正确') 
        else:
            print(f'回答错误，正确答案是{keys[-1]}')
    else:
        if key == keys[3]:
            print('回答正确')
        else:
            print(f'回答错误，正确答案是{keys[3]}')
    i += 1

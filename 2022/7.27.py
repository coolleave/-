# 装饰器的推导
def bg(game):
    def inner():
        print('开挂')
        game()
        print('关挂')
    return inner  # 函数封装


def play_lol():
    print('英雄联盟')


@bg  # play_dnf = bg(play_dnf)  # 新函数的赋值
def play_dnf():
    print('地下城与勇士')


play_dnf()


def wrapper(fn):
    def inner():
        print('脱衣服')
        fn()
        print('穿衣服')
    return inner


@wrapper
def c():
    print('洗澡')


c()
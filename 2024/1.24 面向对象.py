# class people:
#     skin_color = 'yellow'
#
#     def __init__(self):
#         pass
#
#
# p1 = people  # 创建实例
#
# print(p1.skin_color)
# p1.skin_color = 'black'  # 通过是实例修改类属性，python会自动创建一个实例属性，而不会修改类属性
# print(people.skin_color)

# 使用面向对象模拟人狗大战
class Dog:
    type = 'dog'  # 设置类属性

    def __init__(self, name, kind, attack_val):
        self.name = name
        self.kind = kind
        self.attack_val = attack_val
        self.life_val = 100  # 每只狗都有自己生命值

    def bite(self, person):  # 定义咬人方法
        person.life_val -= self.attack_val
        print(f'【{self.name}】咬了【{person.name}】一口，造成了【{self.attack_val}】点伤害，还剩余【{person.life_val}】点血量')


class Person:
    type = 'people'

    def __init__(self, name, age, attack_val):
        self.name = name
        self.age = age
        self.attack_val = attack_val
        self.life_val = 100

    def strike(self, dog):
        dog.life_val -= self.attack_val
        print(f'【{self.name}】攻击了【{dog.name}】，造成了【{self.attack_val}】点伤害，还剩余【{dog.life_val}】点血量')


if __name__ == '__main__':

    d1 = Dog('旺财', '二哈', 14)  # 实例化 狗
    d2 = Dog('大黄', '土狗', 30)

    p1 = Person('小明', 13, 23)  # 实例化人
    p2 = Person('小强', 24, 50)

    d1.bite(p1)  # 旺财 咬 小明
    p2.strike(d2)  # 小强 打 大黄

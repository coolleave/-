class Dog:
    type = 'dog'  # 设置类属性

    def __init__(self, name, kind, attack_val, master):
        self.name = name
        self.kind = kind
        self.attack_val = attack_val
        self.life_val = 100  # 每只狗都有自己生命值
        self.master = master
        self.sayhi()

    def sayhi(self):
        print(f'i am {self.name}, my master is {self.master.name}')

    def bite(self, person):  # 定义咬人方法
        person.life_val -= self.attack_val
        print(f'【{self.name}】咬了【{person.name}】一口，造成了【{self.attack_val}】点伤害，还剩余【{person.life_val}】点血量')


class Weapon:

    def dog_stick(self, obj):
        self.name = '打狗棍'
        self.attack_val = 100
        obj.life_val -= self.attack_val
        self.print_log(obj)

    def print_log(self, obj):
        print(f'【{obj.name}】被【{self.name}】攻击了，造成了【{self.attack_val}】点伤害，还剩余【{obj.life_val}】点血量')


class Person:
    type = 'people'

    def __init__(self, name, age, attack_val):
        self.name = name
        self.age = age
        self.attack_val = attack_val
        self.life_val = 100
        self.weapon = Weapon()  # 在这里实例化，相当于

    def strike(self, dog):
        dog.life_val -= self.attack_val
        print(f'【{self.name}】攻击了【{dog.name}】，造成了【{self.attack_val}】点伤害，还剩余【{dog.life_val}】点血量')


if __name__ == '__main__':
    p1 = Person('小明', 22, 40)  # 实例化主人
    d1 = Dog('happy', 'puppy', 33, p1)  # 将主人传递给狗
    p1.weapon.dog_stick(d1)
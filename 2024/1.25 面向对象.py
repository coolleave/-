# 测试1
def test1():
    # 创建人的类
    class Person:
        # 初始化姓名，年龄，性别，对象
        def __init__(self, name, age, sex):
            self.name = name
            self.age = age
            self.sex = sex
            self.partner = None
    # 创建两个实例
    p1 = Person('小明', 16, 'm')
    p2 = Person('小红', 18, 'w')
    # 将两个实例进行绑定
    p1.partner = p2
    p2.partner = p1
    # 测试,打印名字
    print(p1.partner.name, p2.partner.name)


def test2():
    class Person:
        def __init__(self, name, age, sex):
            self.name = name
            self.age = age
            self.sex = sex

    class relationship:
        relationship_lst = []

        def relationship(self, p1, p2):



if __name__ == '__main__':
    test1()

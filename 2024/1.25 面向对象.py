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
    # 创建Person类
    class Person:
        # 初始化 输入名字 年龄 性别
        def __init__(self, name, age, sex):
            self.name = name
            self.age = age
            self.sex = sex

    # 创建Relationship 类
    class Relationship:
        # 初始化 准备列表存储关系
        def __init__(self):
            self.relationship_lst = []
        # 结婚方法，传入两个变量

        def make_couple(self, obj1, obj2):
            self.relationship_lst = [obj1, obj2]

        # 查询婚姻关系方法
        def check_couple(self, obj):
            # 通过循环找到另一半的实例，返回另一半的实例
            for i in self.relationship_lst:
                if i != obj:
                    # print(i.name)
                    return i
            print(None)

        # 离婚方法，清空列表
        def divorce(self):
            self.relationship_lst = []

    # 将两个人实例化
    p1 = Person('小明', '22', 'm')
    p2 = Person('小红', '20', 'w')
    # 将关系实例化
    rel = Relationship()
    # 两个人结婚
    rel.make_couple(p1, p2)
    # 查询婚姻状态
    print(rel.check_couple(p1).name)
    # 离婚
    rel.divorce()
    # 查询状态
    print(rel.check_couple(p1))


if __name__ == '__main__':
    test2()

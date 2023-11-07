"""
面向对象的三大特征
1、封装 安全性，类似于胶皮裹电线
2、继承
3、多态
"""


def fz():
    class Car:
        def __init__(self, brand, life_span):
            Car.brand = brand
            Car.__life_span = life_span  # 使用寿命不能在外部访问，但是在类的内部可以访问
            # 在属性前面加上两个下划线__就可以实现这种效果

        def show(self):
            print(Car.brand)
            print(Car.__life_span)

    car1 = Car('宝马', 20)

    print(car1.brand)
    # print(car1.__life_span)
    # 但是这种封装方式可以强行访问
    print(dir(Car))
    print(car1._Car__life_span)
    # 使用_Car__life_span 就可以进行外部访问


def jc():
    class Test(object):  # 定义考试，继承万物祖宗object
        def __init__(self, age, name):
            Test.name = name
            self.age = age

    class Test1(Test):  # 定义类对象时，括号里放着的就是他爹
        def __init__(self, age, name, test_number):
            super().__init__(name, age)  # 使用super命令进行继承他爹的属性
            Test.test_number = test_number

    class Test2(Test):
        def __init__(self, age, name, test_level):
            super().__init__(name, age)
            self.test_level = test_level

    # 多继承中总说缺少一个参数。我不理解
    class Test3(Test1, Test2):
        def __init__(self, test_number, test_level):
            super().__init__(test_number, test_level)

    mer = Test1(12, '张三', 222)
    print(mer.name, mer.age, mer.test_number)
    mer2 = Test3(4, '难')
    print(mer2.test_level, mer2.test_number)


if __name__ == '__main__':
    pass
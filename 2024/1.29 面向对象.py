# 静态方法， staticmethod
# 静态方法就是与类和实例隔离开来，不能访问他们的任何方法和变量
def test1():
    class Student:
        def __init__(self, name):
            self.name = name

        @staticmethod
        def walk():
            print('he is walking')

        @staticmethod
        def eat(self):
            print(self.name, 'is eating')

    s = Student('coolleave')
    s.walk()  # 静态方法的调用
    s.eat(s)  # 如果非要静态方法使用实例的变量，就需要把实例作为参数传进去


# 方法变成静态属性
def test2():
    class Flight:
        def __init__(self):
            pass

        # 方法变成静态属性
        @property
        def resp(self):
            print('flight is readying')

    f = Flight()
    f.resp  # 调用方法时，可以不加括号，此时的方法和属性有些类似


if __name__ == '__main__':
    test1()

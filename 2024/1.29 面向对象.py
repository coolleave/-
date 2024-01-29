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


# 反射（也叫映射、自省）
"""
反射可以让程序在运行时检查并修改自身的结构，
使得程序能够根据需要动态地创建对象、调用方法、获取和修改属性等。
通过反射，程序可以在运行时获取到类的信息、方法的签名、注解等，并根据这些信息进行相应的操作。
反射一共有四种方法
hasattr   判断
getattr   获取
# 获取对象的属性值
value = getattr(obj, 'attr')
print(value)  # 输出：10

# 获取对象的方法，并调用
method = getattr(obj, 'my_method')
method()  # 输出：This is my method

# 获取对象不存在的属性值，默认返回 None
value = getattr(obj, 'nonexistent_attr')
print(value)  # 输出：None

# 获取对象不存在的方法，默认返回 None
method = getattr(obj, 'nonexistent_method')
print(method)  # 输出：None

# 获取对象不存在的属性值，自定义默认值
value = getattr(obj, 'nonexistent_attr', 0)
print(value)  # 输出：0
setattr   赋值
delattr   删除
"""


def test3():
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age

        @staticmethod
        def method():
            print(124)
            return 1

        def reflection(self):
            # if hasattr(self, 'name1'):  # 判断实例中是否有name1属性
            #     print('yes')

            a = getattr(p, 'name')
            print(a())
    p = Person('coollave', '20')
    p.reflection()


if __name__ == '__main__':
    test3()

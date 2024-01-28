"""
类方法 在类方法中，只能访问类变量，而不能访问实例变量
原因 ： 在方法传参中，传参的传入的是类（cla），而不是实例本身（self）

"""


def test1():
    class Stduent:
        def __init__(self, name):
            self.name = name

        @classmethod
        def eat(cls):
            # print(cls.name)  # 会报错:type object 'Stduent' has no attribute 'name'
            pass

        def eat_(self):
            print(self.name)  # 正常显示

    s = Stduent('haha')
    s.eat()
    s.eat_()


"""
小练习
创建一个学生类，每创建一个学生实例，打印一共创建了多少个学生实例
"""


def test2():
    class Student:
        stu_num = 0

        def __init__(self, name):
            self.name = name
            Student.stu_num = Student.stu_num + 1  # self.变量名对实例进行赋值，类名.变量名 是对类进行赋值
            print(self.name, Student.stu_num)

    s1 = Student('S1')
    s2 = Student('s2')
    s3 = Student('s3')

# 对于test2的补充


def test3():
    class Stduent:
        stu_num = 0

        def __init__(self, name):
            self.name = name
            self.__add()
            print(Stduent.stu_num)

        @classmethod
        def __add(cls):
            Stduent.stu_num += 1

    s1 = Stduent('mike')
    s2 = Stduent('amy')
    s3 = Stduent('frank')


if __name__ == '__main__':
    test3()

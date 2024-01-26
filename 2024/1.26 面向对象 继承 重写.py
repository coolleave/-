"""
当谈到类的继承时，
可以创建一个新的类，
并从现有的类中继承属性和方法。
继承的类称为子类或派生类，被继承的类称为父类或基类。
子类可以访问和使用父类的属性和方法。
"""


def test1():
    # define baseclass
    class Animal:
        # define default function
        def __init__(self, name):
            self.name = name

        def eating(self):
            print(f'{self.name} is eating')
    # define subclass base on Animal

    class Dog(Animal):
        def eating1(self):
            print(self.name, 'is playing')

    d1 = Dog('x')
    d1.eating()
    d1.eating1()


"""
重写（Override）是指在子类中重新定义父类的方法。
当子类重写父类的方法时，子类会使用自己的实现替代父类的实现。
"""


def test2():
    # define  baseclass
    class Animal:
        def sound(self):
            print('animal makes sound')

    # define subclass
    class Dog(Animal):
        # override method sound
        def sound(self):
            print('dog makes sound')

    # create instances
    a = Animal()
    d = Dog()

    # call the method
    a.sound()  # animal makes sound
    d.sound()  # dog makes sound


if __name__ == '__main__':
    test2()

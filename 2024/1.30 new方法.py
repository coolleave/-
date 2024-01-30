# __new__ 方法在init方法之前执行，并且init方法是由new方法调用的，
# 如果将new方法重写了，没有调用init，init就不会自动执行
def test1():
    class Person:
        def __init__(self, name):
            self.name = name
            print('init 被调用了')

        def __new__(cls, *args, **kwargs):
            print('new 被调用了')

    p = Person('coolleave')


"""
以上例子得出结论，重写new方法后，init没有被调用

"""


# 单例模式
def test2():
    class Printer:
        tasks = []
        instance = None

        def __init__(self, name):
            self.name = name
            print(self.name, '被创建了')

        def add_task(self, job):
            self.tasks.append(job)
            print(f'{job}被{self.name}添加到了任务栏中，此时的任务有{len(self.tasks)}')

        def __new__(cls, *args, **kwargs):
            if cls.instance is None:  # 判断是否有实例存在
                cls.instance = super().__new__(cls)  # 如果不存在，创建一个实例
            return cls.instance  # 直接返回实例

        def __call__(self, *args, **kwargs):
            print('call被调用了')

    p1 = Printer('word')
    p2 = Printer('excel')
    p3 = Printer('edge')

    p1.add_task('word file')
    p2.add_task('excel file')
    p3.add_task('pdf file')
    p3()  # 实例后加括号 就会调用call方法
    print(p1,p2,p3)


# 使用类方法 应用单例模式
def test3():
    class Student:
        _instance = None

        def __init__(self):
            if not Student._instance:
                Student._instance = self
                print('created a instance')
            else:
                print('instance already created')
                self.getinstance()

        @classmethod
        def getinstance(cls):
            if not cls._instance:
                cls._instance = Student()
            return cls._instance

    s1 = Student()
    s2 = Student.getinstance()
    s3 = Student.getinstance()
    print(s1)
    print(s2)
    print(s3)


if __name__ == '__main__':
    test3()

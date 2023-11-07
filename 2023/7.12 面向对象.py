"""


class Student:  # 使用驼峰命名法规范，首字母大写
    native_place = '平泉'  # 直接写在类里的变量叫做类属
    # 在类之外定义的称为函数，在类之内定义的成为方法
    # 实例方法
    def __init__(self,name, age):
        print('我是初始化定义')
        self.name = name   # self.name 是实体属性，进行了一个赋值操作，将局部变量的值赋值给实体属性
        self.age = age

    def eat(self):  # 加一个self
        print('我是实例方法')

    @staticmethod
    def eat1():
        print('我是静态方法，因为我使用了staticmethod修饰')

    @classmethod
    def eat2(cls):  # 类方法，加一个（cls）
        print('我是类方法，因为我使用了class——method修饰')


print(id(Student))  # 对象Student 的内存地址
print(type(Student))  # 对象Student 的类型
print(Student)  # 对象Student的value

# 根据类对象创建实例对象
xs = Student('张三', 20)
print(id(xs))
print(type(xs))
print(xs)


# 创建实例对象
stu1 = Student('张三', 20)
stu2 = Student('李四', 21)
stu3 = Student('王五', 20)
print(stu1.native_place)
print(stu2.native_place)
print(stu3.native_place)


"""


class Student:
    native_school = '平泉一中'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f'{self.name}在吃饭')


stu1 = Student('张三', 20)
stu2 = Student('李四', 19)
stu1.gender = '男'  # 使用动态属性绑定实例对象
print(stu1.gender, stu1.name, Student.eat(stu1), stu1.native_school)


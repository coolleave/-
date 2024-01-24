class dog:
    d_type = '二哈'  # 类属性，类变量
    # 类外的def 叫函数，类内的def 叫方法

    def __init__(self, name, age):
        # 初始化方法，也叫构造方法，构造函数。实例化时会自动执行，进行一些初始化操作。
        # 实例化时候传的参数对应的就是初始化方法的参数

        # 将实例与传进来的参数进行绑定，就能把参数真正存到实例里。
        self.name = name
        self.age = age

    def say_hi(self):  # 方法第一个参数必须是self，代表实例本身
        print('i am a dog , my name is', self.name)


d = dog('hh', '2')  # 生成一个实例

d.sex = '母'  # 为实例增加一个属性，就相当于在 __init__ 中增加一个属性
if __name__ == '__main__':
    d.say_hi()  # 实例.方法
    print(d.d_type)  # 实例.属性

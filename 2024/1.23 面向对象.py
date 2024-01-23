class dog:
    d_type = '二哈'  # 类属性，类变量

    def say_hi(self):  # 代表实例本身
        print('i am a dog , my name is', self.d_type)


d = dog()  # 生成一个实例
if __name__ == '__main__':
    d.say_hi()

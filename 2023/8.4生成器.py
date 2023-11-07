"""
迭代器统一了容器类型循环遍历的标准
for 循环运用的就是统一的循环方式，可迭代协议，for循环运用的就是迭代器
iterable:可迭代的
int类型是不可迭代的
坑
1、想要迭代器重新迭代，需要再拿一遍迭代器
2、这里不适合数学上的等价代换

可迭代的不一定是迭代器，比如列表
但迭代器一定是可迭代的

迭代器的特点
1、节省内存
2、惰性机制
3、只能向下迭代，不可逆

生成器 生成器的本质就是迭代器
当函数中有yield时就是一个生成器函数
yield就是返回，当调用next的到时候，就会返回

列表推导式公式  [结果  for循环 if条件]
python 中没有元组推导式
有 列表推导式，字典推导式，集合推导式，但是没有元组推导式


拿空生成器的方案
1、直接用for循环
2、直接转化为列表，元组等容器类数据类型

匿名函数 又叫做lambda表达式
格式 lambda 参数： 返回值
通过lambda创建的函数统一叫做lambda
写很简单的操作懒得起名
函数的参数要用逗号隔开
只能写一行，尽量简单
返回多个数据时要手动加小括号变成元组
"""

lst = ['c', 'c++', 'java', 'python']


def meet():
    it = lst.__iter__()  # 包装成迭代器
    print(dir(it))  # 查看目标对象能执行的操作
    print(type(it))  # 查看数据类型
    it.__next__()  # 进行下一个


# 模拟for循环的大致过程
def for_():
    it = lst.__iter__()
    while True:
        try:
            i = it.__next__()
            print(i)
        except StopIteration:
            break


# 列表推导式
def lst1():
    lst2 = []
    for i in range(1, 10):
        lst2.append(i)
    print(lst2)
    lst2 = [i for i in range(1, 14) if i % 2 == 1]
    print(lst2)
    lst3 = [f'python{t}' for t in range(1, 1000)]
    print(lst3)


if __name__ == '__main__':
    lst1()
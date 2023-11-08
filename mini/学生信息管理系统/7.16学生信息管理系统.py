import os
import time


# 定义各个功能的函数

# 定义保存函数
def save(lst):
    with open('student.txt', mode='a', encoding='utf-8') as f:
        for i in lst:
            f.write(str(i))  # i对象为字典，需要格式化为字符串
            f.write('\n')
    print('信息保存成功')


# 定义主菜单函数
def main():
    # 设置菜单界面
    while 1:
        print('========================学生信息管理系统========================\n'
              '----------------------------功能菜单---------------------------\n',
              '                        1、增加学生\n',
              '                        2、删除学生\n',
              '                        3、修改学生信息\n',
              '                        4、查找学生\n',
              '                        5、对学生进行排序\n',
              '                        6、统计学生总数\n',
              '                        7、显示所有学生信息\n',
              '                        0、退出系统')
        print('----------------------------功能菜单---------------------------')
        a = input('请输入数字编号\n')  # 接收数字选项
        # 设置退出系统功能
        if a == '0':
            b = input('确定要退出系统吗？ y/n\n')
            if b == 'y' or b == 'Y':
                print('感谢您的使用')
                break  # 退出循环，程序结束
            else:
                continue  # 退出本次循环，进入下一次循环
        # 格式化选项，判断是否能格式化为数字
        if a == '1':
            add()
        if a == '2':
            delete()
        if a == '3':
            change()
        if a == '4':
            find()
            break
        if a == '5':
            sort()
            break
        if a == '6':
            tj()
        if a == '7':
            show()
        else:
            print('请按照要求输入数字')


# 定义增加函数
def add():
    while True:
        lst = []
        while True:
            number = input('请输入学号，如1001\n')
            try:
                number = int(number)
                break
            except ValueError:
                print('输入有误！！！请重新输入')
                continue
        name = input('请输入姓名\n')
        while True:
            english = input('请输入英语成绩\n')
            try:
                english = float(english)
                break
            except ValueError:
                print('输入有误！！！请重新输入')
                continue
        while True:
            math = input('请输入数学成绩\n')
            try:
                math = float(math)
                break
            except ValueError:
                print('输入有误！！！请重新输入')
                continue
        while True:
            chinese = input('请输入语文成绩\n')
            try:
                chinese = int(chinese)
                break
            except ValueError:
                print('输入有误！！！请重新输入')
                continue
        lst.append({'学号': f'{number}', '姓名': f'{name}',
                    '英语成绩': f'{english}',
                    '语文成绩': f'{chinese}', '数学成绩': f'{math}'})  # 字典加入列表
        save(lst)
        choice = input('是否继续添加? y/n\n')
        if choice == 'y':
            continue
        else:
            break


# 定义删除信息函数
def delete():
    while True:
        num = input('请输入学号\n')
        if os.path.exists('student.txt'):  # 判断是否存在文件
            # 边读边写
            with open('student.txt', 'r', encoding='utf-8')as old_file:
                old_line = old_file.readlines()  # 读取文件
        else:
            old_line = []
        flag = False  # 删除标志
        if old_line:  # 文件不为空
            with open('student.txt', 'w', encoding='utf-8') as f:  # 写入文件
                for item in old_line:  # 遍历读取的文件
                    d = dict(eval(item))
                    # print(d)
                    if d['学号'] != num:
                        f.write(str(d) + '\n')
                        # print(str(d))
                    else:
                        flag = True

                if flag:
                    print(f'学号为{num}的学生信息已经删除！')
                else:
                    print('没有找到相应学号的学生')
                show()
        else:
            print('没有任何学生信息')
            break
        choice = input('是否继续删除?  y/n\n')
        if choice == 'y':
            continue
        else:
            print('返回菜单界面')
            break


# 定义更改信息函数
def change():
    show()
    if os.path.exists('student.txt'):
        with open('student.txt', mode='r', encoding='utf-8') as r:
            old_lines = r.readlines()
    else:
        return
    if old_lines:
        num = input('请输入学号\n')
        try:
            num = int(num)
        except ValueError:
            print('输入的学号有误，请重新输入')
            change()
        with open('student.txt', 'w', encoding='utf-8') as w:
            for line in old_lines:
                d = dict(eval(line))  # 将读取到的str转化为字典格式
                flag = False  # 是否修改标识
                if d['学号'] == str(num):
                    print(f'已经找到{num}请进行修改')
                    d['姓名'] = input('请输入姓名\n')
                    while True:
                        d['英语成绩'] = input('请输入英语成绩\n')
                        try:
                            d['英语成绩'] = float(d['英语成绩'])
                            break
                        except ValueError:
                            print('输入有误！！！请重新输入')
                            continue
                    while True:
                        d['数学成绩'] = input('请输入数学成绩\n')
                        try:
                            d['数学成绩'] = float(d['英语成绩'])
                            break
                        except ValueError:
                            print('输入有误！！！请重新输入')
                            continue
                    while True:
                        d['语文成绩'] = input('请输入语文成绩\n')
                        try:
                            d['语文成绩'] = int(d['语文成绩'])
                            break
                        except ValueError:
                            print('输入有误！！！请重新输入')
                            continue
                    flag = True
                    # print('修改后', str(d))
                    w.write(str(d) + '\n')
                else:
                    # print('没有修改', str(d))
                    w.write(str(d) + '\n')
        if flag:
            print('修改完成')
        else:
            print(f'没有找到学号{num}')

        a = input('是否需要继续修改? y/n\n')
        if a == 'y':
            change()
        else:
            print('三秒后将返回主菜单')
            main()
    else:
        print('没有任何学生信息, 3秒后将返回主菜单')
        time.sleep(3)
        main()


# 定义查找信息函数
def find():
    if os.path.exists('student.txt'):
        with open('student.txt', 'r', encoding='utf-8') as r:
            lines = r.readlines()
        if lines:
            mode = input('请选择查找模式，按学号查找请输入1， 按姓名查找请输入2\n')
            if mode == '1':
                lst = []
                num = input('请输入要查找的学号\n')
                flag = False
                for line in lines:
                    line = dict(eval(line))
                    if line['学号'] == num:
                        flag = True
                        lst.append(line)
                present(lst)
                if flag:
                    print('已经找到啦')
                else:
                    print('并没有找到，请重新输入吧')
                    find()
            elif mode == '2':
                lst = []
                name = input('请输入要输入的名字\n')
                flag = False
                for line in lines:
                    line = dict(eval(line))
                    if line['姓名'] == name:
                        lst.append(line)
                        flag = True
                present(lst)
                if flag:
                    print('已经找到啦')
                else:
                    print('并没有找到，请重新输入吧')
                    find()
            else:
                print('按学号查找请输入1， 按姓名查找请输入2')
                find()
        else:
            print('没有学生信息')
    else:
        print('没有任何学生信息，3秒后将返回主菜单')
        time.sleep(3)
        main()
    choice = input('是否要继续查找？y/n\n')
    if choice == 'y':
        find()
    else:
        print('3秒后回到主菜单')
        time.sleep(3)
        main()


# 定义查找显示函数
def present(lst):
    if lst:
        num = '学号'
        name = '姓名'
        chinese = '语文'
        math = '数学'
        english = '英语'
        total = '总成绩'
        print(f'{num:^6}{name:^12}{chinese:^8}{math:^10}{english:^10}{total:^8}')
        for i in lst:
            num = i['学号']
            name = i['姓名']
            chinese = i['语文成绩']
            math = i['数学成绩']
            english = i['英语成绩']
            total = float(chinese)+float(math)+float(english)
            print(f'{num:^10}{name:^12}{chinese:^10}{math:^10}{english:^15}{total:^12}')
    else:
        print('没有查询到内容，请重新输入吧')
        find()


# 定义排序信息函数
def sort():
    # 选择模式
    global sx
    mode = input('请选择排序方式0.正叙 1.倒叙  \n')
    if mode == '1':  # 将bool值设置成true
        sx = True
    elif mode == '0':
        sx = False
    else:
        print('请输入正确的数字1或者0')
        sort()
    lst = []
    # 打开文件
    with open('student.txt', mode='r', encoding='utf-8') as r:
        lines = r.readlines()
        for line in lines:
            student = dict(eval(line))
            lst.append(student)  # 将学生加入列表
        # 选择排序的项目
        while 1:
            pro = input('请选择排序的依据，1.学号2.语文成绩3.数学成绩4.英语成绩5.总成绩\n')
            if pro == '1':  # 这里使用的匿名函数 提取字典里的value
                lst.sort(key=lambda x: int(x['学号']), reverse=sx)  # 运用bool值来确定顺序
            elif pro == '2':
                lst.sort(key=lambda x: int(x['语文成绩']), reverse=sx)
            elif pro == '3':
                lst.sort(key=lambda x: int(x['数学成绩']), reverse=sx)
            elif pro == '4':
                lst.sort(key=lambda x: int(x['英语成绩']), reverse=sx)
            elif pro == '5':
                lst.sort(key=lambda x: float(x['语文成绩']) + float(x['数学成绩']) + float(x['英语成绩']), reverse=sx)
            else:
                print('请输入正确的数字')
            present(lst)  # 将列表传给present函数，完成了函数的重复利用
            break
    main()


# 定义统计信息函数
def tj():
    if os.path.exists('student.txt'):
        with open('student.txt', 'r', encoding='utf-8') as f:
            lines = f.readlines()
            if len(lines) == 0:  # 判断列表长度来判断学生信息数量
                print('没有信息')
                input('输入任意键返回\n')
                main()
            else:
                print(f'一共有{len(lines)}个学生')
                input('输入任意键返回\n')
                main()
    else:
        print('没有信息')


# 定义展示信息函数
def show():
    if os.path.exists('student.txt'):
        with open('student.txt', 'r', encoding='utf-8') as r:
            lines = r.readlines()
            if lines:
                num = '学号'
                name = '姓名'
                chinese = '语文'
                math = '数学'
                english = '英语'
                total = '总成绩'
                print(f'{num:^6}{name:^12}{chinese:^8}{math:^10}{english:^10}{total:^8}')
                for i in lines:
                    i = dict(eval(i))
                    num = i['学号']
                    name = i['姓名']
                    chinese = i['语文成绩']
                    math = i['数学成绩']
                    english = i['英语成绩']
                    total = float(chinese) + float(math) + float(english)
                    print(f'{num:^10}{name:^12}{chinese:^10}{math:^10}{english:^15}{total:^12}')
            else:
                print('没有信息')
            input('按任意键返回主菜单\n')
            main()


if __name__ == '__main__':
    main()

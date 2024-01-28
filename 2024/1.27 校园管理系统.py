# 创建总校类
class School:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def pay_wage(self):  # 发工资方法
        pass

    def count_staff_num(self):  # 统计员工人数
        pass

    def count_stu_num(self):  # 统学员人数
        pass

    def new_stu(self):  # 新员工注册
        pass


# 创建分校类，并且继承总校类
class BranchSchool(School):
    def __init__(self, name, address, schoolbase):
        super().__init__(name, address)
        self.schoolbase_name = schoolbase.name

    def check_information(self):
        print("分校名称:", self.name)
        print("所属总校:", self.schoolbase_name)


# 创建班级类，继承分校类
class Class:
    def __init__(self, class_num, course_obj, branchschool):
        self.class_num = class_num
        self.course_obj = course_obj
        self.branchschool = branchschool
        lst_stu = []  # 创建学员名单

    def create_teaching_record(self):
        print(self.class_num, 'created a record')

    def drop_out(self):
        pass

    def check_information(self):
        print('班级编号', self.class_num, '课程', self.course_obj, '所属分校', self.branchschool.name)


# 创建课程类
class Course:
    def __init__(self):
        pass


# 创建学生类
class Student:
    def __init__(self, name, age, gender, learn_obj, classbase):
        self.name = name
        self.age = age
        self.gender = gender
        self.learn_obj = learn_obj
        self.classbase = classbase
        print(f'新来了一个学员{name}，年龄{age}， 性别{gender}，ta报名的科目是{learn_obj}')
        self.classbase.lst_stu.append(self.name, self.age, self.gender, self.learn_obj)


# 创建员工类
class Stuff:
    def __init__(self, name, age, gender, teach_obj):
        self.name = name
        self.age = age
        self.gender = gender
        self.teach_obj = teach_obj
        print(f'新来了一个员工{name}，年龄{age}， 性别{gender}，ta报名的科目是{teach_obj}')

# 创建教师类，并继承员工类


class Teacher(Stuff):
    def __init__(self, name, age, gender, teach_obj):
        super().__init__(name, age, gender, teach_obj)


school = School('总校', '河北省')
branch_school = BranchSchool('分校', '石家庄市', school)
class1 = Class(1, 'python', branch_school)
class1.check_information()

# print(branch_school.check_information())


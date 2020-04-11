import os, pickle, uuid
from conf.settings import DB_USER_DIR



class FileMixin:

    @classmethod
    def get_obj(cls, name):
        file_path = os.path.join(DB_USER_DIR, cls.__name__, f'{name}.pkl')
        if os.path.isfile(file_path):
            with open(file_path, 'rb') as f:
                return pickle.load(f)


    def save_obj(self, obj):
        file_dir = os.path.join(DB_USER_DIR, self.__class__.__name__)
        if not os.path.isdir(file_dir):
            os.mkdir(file_dir)
        file_path = os.path.join(file_dir, f'{obj.name}.pkl')
        with open(file_path, 'wb') as f:
            pickle.dump(obj, f)


class Admin(FileMixin):
    def __init__(self, name, pwd):
        self.name = name
        self.pwd = pwd
        self.save_obj(self)


class School(FileMixin):
    def __init__(self, name, addr):
        self.name = name
        self.addr = addr
        self.id = str(uuid.uuid4())
        self.class_list = []
        self.teacher_list = []
        self.course_list = []
        self.save_obj(self)

    def __str__(self):
        txt_info = f'{self.name.center(50, "-")}\n' \
                   f'班级：{",".join(self.class_list)}\n' \
                   f'讲师：{",".join(self.teacher_list)}\n' \
                   f'课程：{",".join(self.course_list)}\n'
        return txt_info

    def create_class(self, class_name):
        Class(self.name, class_name)
        self.class_list.append(class_name)
        self.save_obj(self)

    def create_course(self, course_name, period, price):
        Course(course_name, period, price)
        self.course_list.append(course_name)
        self.save_obj(self)


class Class(FileMixin):
    def __init__(self, sch_name, class_name):
        self.name = class_name
        self.sch_name = sch_name
        self.course_list = []
        self.teacher_list = []
        self.student_list = []
        self.save_obj(self)

    def __str__(self):
        txt_info = f'{self.name.center(50, "-")}\n' \
                   f'校区：{self.sch_name}\n' \
                   f'课程：{",".join(self.course_list)}\n' \
                   f'讲师：{",".join(self.teacher_list)}\n' \
                   f'学生：{",".join(self.student_list)}\n'
        return txt_info

    def relate_course(self, course_name):
        self.course_list.append(course_name)
        self.save_obj(self)

    def relate_student(self, stu_name):
        self.student_list.append(stu_name)
        self.save_obj(self)



class Course(FileMixin):
    def __init__(self, course_name, period, price):
        self.name = course_name
        self.period = period
        self.price = price
        self.save_obj(self)

    def __str__(self):
        return f'课程：{self.name} 周期：{self.period}月 价格：{self.price}元'


class Teacher(FileMixin):
    def __init__(self, sch_name, teacher_name, level, pwd):
        self.name = teacher_name
        self.pwd = pwd
        self.level = level
        self.sch_name = sch_name
        self.class_list = []
        self.save_obj(self)

    def __str__(self):
        txt_info = f'{self.name.center(50, "-")}\n' \
                   f'等级：{self.level}\n' \
                   f'学校：{self.sch_name}\n' \
                   f'班级：{",".join(self.class_list)}\n'
        return txt_info


class Student(FileMixin):
    def __init__(self, sch_name, class_name, stu_name, age, sex, pwd):
        self.sch_name = sch_name
        self.class_name = class_name
        self.name = stu_name
        self.age = age
        self.sex = sex
        self.pwd = pwd
        self.score = None
        self.__is_pay_tuition = False
        self.course = []
        self.save_obj(self)

    def __str__(self):
        txt_info = f'{self.name.center(50, "-")}\n' \
                   f'年龄：{self.age}\n' \
                   f'性别：{self.sex}\n' \
                   f'课程：{self.course}\n' \
                   f'分数：{",".join(self.score)}\n'
        return txt_info


    def select_course(self, course_name):
        self.course.append(course_name)
        self.save_obj(self)


    @property
    def is_pay_tuition(self):
        return self.__is_pay_tuition


    def pay_tuition(self, amounts):
        if amounts > 20000:
            self.__is_pay_tuition = True
            self.save_obj(self)
            return True, '缴费成功'
        else:
            return False, '缴费金额不足20000'
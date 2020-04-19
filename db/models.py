import sys
from conf import settings
from db import db_handle


class FileMixin:

    @classmethod
    def get_obj(cls, name):
        return db_handle.get_obj(cls, name)

    def save_obj(self):
        db_handle.save_obj(self)


class Human:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
        self.__pwd = settings.INIT_PWD
        self.role = self.__class__.__name__

    @property
    def pwd(self):
        return self.__pwd

    @pwd.setter
    def pwd(self, new_pwd):
        self.__pwd = new_pwd


class Admin(FileMixin, Human):

    def __init__(self, name, age, sex):
        super().__init__(name, age, sex)
        self.save_obj()

    @staticmethod
    def create_school(school_name, school_addr):
        School(school_name, school_addr)

    @staticmethod
    def create_course(school_name, course_name, course_period, course_price):
        Course(course_name, course_period, course_price, school_name)

    @staticmethod
    def create_teacher(teacher_name, teacher_age, teacher_sex, teacher_level):
        Teacher(teacher_name, teacher_age, teacher_sex, teacher_level)

    @staticmethod
    def create_student(stu_name, stu_age, stu_sex, school_name, homeland):
        Student(stu_name, stu_age, stu_sex, school_name, homeland)

    @staticmethod
    def reset_user_pwd(name, role):
        obj = getattr(sys.modules[__name__], role).get_obj(name)
        obj.pwd = settings.INIT_PWD
        obj.save_obj()


class School(FileMixin):
    def __init__(self, name, addr):
        self.name = name
        self.addr = addr
        self.course_list = []
        self.save_obj()

    def relate_course(self, course_name):
        self.course_list.append(course_name)
        self.save_obj()


class Course(FileMixin):
    def __init__(self, name, period, price, school_name):
        self.name = name
        self.period = period
        self.price = price
        self.school = school_name
        self.teacher = None
        self.student_list = []
        self.save_obj()

    def relate_teacher(self, teacher_name):
        self.teacher = teacher_name
        self.save_obj()

    def relate_student(self, stu_name):
        self.student_list.append(stu_name)
        self.save_obj()


class Teacher(FileMixin, Human):
    def __init__(self, name, age, sex, level):
        super().__init__(name, age, sex)
        self.level = level
        self.course_list = []
        self.save_obj()

    def select_course(self, course_name):
        self.course_list.append(course_name)
        self.save_obj()
        course_obj = Course.get_obj(course_name)
        course_obj.relate_teacher(self.name)

    def check_my_courses(self):
        return self.course_list

    @staticmethod
    def check_my_student(course_name):
        course_obj = Course.get_obj(course_name)
        return course_obj.student_list

    @staticmethod
    def set_score(stu_name, course_name, score):
        stu_obj = Student.get_obj(stu_name)
        stu_obj.score_dict[course_name] = int(score)
        stu_obj.save_obj()


class Student(FileMixin, Human):
    def __init__(self, name, age, sex, school_name, homeland):
        super().__init__(name, age, sex)
        self.school = school_name
        self.homeland = homeland
        self.course_list = []
        self.score_dict = {}
        self.save_obj()

    def select_course(self, course_name):
        self.course_list.append(course_name)
        self.score_dict[course_name] = None
        self.save_obj()
        course_obj = Course.get_obj(course_name)
        course_obj.relate_student(self.name)

    def check_my_course(self):
        return self.course_list

    def check_my_score(self):
        return self.score_dict
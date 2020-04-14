from conf import settings
from db import db_handle



class FileMixin:

    @classmethod
    def get_obj(cls, name):
        return db_handle.get_obj(cls, name)

    def save_obj(self):
        db_handle.save_obj(self)


class Human():
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
        self.__pwd = settings.INIT_PWD
        self.role = self.__class__.__name__

    def edit_password(self, new_pwd):
        self.__pwd = new_pwd




class Admin(FileMixin, Human):

    def __init__(self, name, age, sex):
        super().__init__(name, age, sex)
        self.save_obj()

    def create_school(self, school_name, school_addr):
        School(school_name, school_addr)

    def create_course(self, school_name, course_name, course_period, course_price):
        Course(course_name, course_period, course_price, school_name)

    def create_teacher(self, teacher_name, teacher_age, teacher_sex, teacher_level):
        Teacher(teacher_name, teacher_age, teacher_sex, teacher_level)

    def create_student(self, stu_name, stu_age, stu_sex, school_name, homeland):
        Student(stu_name, stu_age, stu_sex, school_name, homeland)

    def reset_user_pwd(self, name, role):
        pass


    def edit_password(self, new_pwd):
        super().edit_password(new_pwd)
        self.save_obj()



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

    def edit_password(self, new_pwd):
        super().edit_password(new_pwd)
        self.save_obj()

    def select_course(self, course_name):
        self.course_list.append(course_name)
        self.save_obj()

    def check_my_courses(self):
        return self.course_list




class Student(FileMixin, Human):
    def __init__(self, name, age, sex, school_name, homeland):
        super().__init__(name, age, sex)
        self.school = school_name
        self.homeland = homeland
        self.course_list = []
        self.score_dict = {}
        self.save_obj()


    def edit_password(self, new_pwd):
        super().edit_password(new_pwd)
        self.save_obj()



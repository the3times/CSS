from conf.settings import INIT_PWD
from db import db_handle
from lib.tools import hash_md5


class Human:
    def __init__(self, name):
        self.name = name
        self.pwd = hash_md5(INIT_PWD)


    def edit_profile(self):
        pass


class FileMixin:
    @classmethod
    def get_obj(cls, name):
        obj = db_handle.get_obj(cls, name)
        return obj

    def save_obj(self):
        db_handle.save_obj(self)



class Admin(FileMixin, Human):
    def __init__(self, name):
        super().__init__(name)
        self.save_obj()

    def create_school(self, school_name, school_addr):
        School(school_name, school_addr)

    def create_course(self, school_obj, course_name, course_period, course_price):
        Course(course_name, course_period, course_price)
        school_obj.relate_course(course_name)

    def create_teacher(self, teacher_name):
        Teacher(teacher_name)

    def create_student(self, stu_name):
        Student(stu_name)



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
    def __init__(self, name, period, price):
        self.name = name
        self.period = period
        self.price = price
        self.student_list = []
        self.save_obj()

    def relate_stu(self, stu_name):
        self.student_list.append(stu_name)
        self.save_obj()

    def get_stu_list(self):
        return self.student_list


class Teacher(FileMixin, Human):
    def __init__(self, name):
        super().__init__(name)
        self.course = None
        self.save_obj()


    def select_course(self, course_name):
        self.course = course_name
        self.save_obj()

    def get_my_course(self):
        return self.course

    def get_my_student_list(self):
        if self.course:
            return Course.get_obj(self.get_my_course()).student_list

    def set_score(self, stu_name, score):
        stu_obj = Student.get_obj(stu_name)
        stu_obj.score[self.course] = score
        stu_obj.save_obj()






class Student(FileMixin, Human):
    def __init__(self, name):
        super().__init__(name)
        self.school = None
        self.course_list = []
        self.score = {}
        self.save_obj()


    def select_school(self, school_name):
        if not self.school:
            self.school = school_name
            self.save_obj()


    def select_course(self, course_name):
        self.course_list.append(course_name)
        self.score[course_name] = None
        self.save_obj()
        course_obj = Course.get_obj(course_name)
        course_obj.relate_stu(self.name)


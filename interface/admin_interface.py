from db import models
from interface import common_interface



def register_interface(name):
    admin_obj = models.Admin.get_obj(name)
    if admin_obj:
        return False, '管理员已经存在, 不能再次注册'
    models.Admin(name)
    return True, f'管理员[{name}]注册成功'




def create_school_interface(school_name, addr, admin_obj_name):
    school_obj = models.School.get_obj(school_name)
    if school_obj:
        return False, f'学校[{school_name}]已经存在'
    admin_obj = models.Admin.get_obj(admin_obj_name)
    admin_obj.create_school(school_name, addr)
    return True, f'学校[{school_name}]创建成功'


def create_course_interface(school_name, course_name, course_period, course_price, admin_name):
    school_obj = models.School.get_obj(school_name)
    if course_name in school_obj.course_list:
        return f'[{course_name}]课程已经存在'

    admin_obj = models.Admin.get_obj(admin_name)
    admin_obj.create_course(school_obj, course_name, course_period, course_price)
    return f'[{course_name}]课程创建成功'


def create_teacher_interface(teacher_name, admin_name):
    teacher_obj = models.Teacher.get_obj(teacher_name)
    if teacher_obj:
        return False, f'[{teacher_name}]老师已经存在'

    admin_obj = models.Admin.get_obj(admin_name)
    admin_obj.create_teacher(teacher_name)
    return True, f'[{teacher_name}]老师创建成功!'


def create_student_interface(stu_name, admin_name):
    stu_obj = models.Student.get_obj(stu_name)
    if stu_obj:
        return False, f'[{stu_name}]学生已经存在'

    admin_obj = models.Admin.get_obj(admin_name)
    admin_obj.create_student(stu_name)
    return True, f'[{stu_name}]学生创建成功!'

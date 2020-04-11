from db.models import Admin, School, Class, Teacher, Student
from db import db_handle
import core.login_user



def register_interface(name, pwd):
    """
    管理员注册接口
    :param name:
    :param pwd: 密文
    :return:
    """
    admin_obj = Admin.get_obj(name)
    if admin_obj:
        return False, '用户名已经存在请换一个'

    Admin(name, pwd)
    return True, '注册成功'


def login_interface(name, pwd):
    """
    管理员登录接口
    :param name:
    :param pwd: 密文
    :return:
    """
    admin_obj = Admin.get_obj(name)
    if not admin_obj:
        return False, '用户名不存在'

    if pwd != admin_obj.pwd:
        return False, '密码错误'
    # 登录成功时
    core.login_user.login_user[:] = [name]
    return True, '登录成功'


def create_school_interface(sch_name, sch_addr):
    sch_obj = School.get_obj(sch_name)
    if sch_obj:
        return False, '学校名已经存在请换一个'
    sch_obj = School(sch_name, sch_addr)
    return True, f'学校:{sch_obj.name}创建成功'


def create_class_interface(sch_name, class_name):
    sch_obj = School.get_obj(sch_name)
    if not sch_obj:
        return False, f'学校:{sch_name}不存在'
    if class_name in sch_obj.class_list:
        return False, f'班级:{class_name}已经存在'

    sch_obj.create_class(class_name)
    return True, f'班级:{class_name}创建成功'


def create_course_interface(sch_name, class_name, course_name, period, price):
    sch_obj = School.get_obj(sch_name)
    if not sch_obj:
        return False, f'学校:{sch_name}不存在'
    if course_name in sch_obj.class_list:
        return False, f'课程:{course_name}已经存在'
    if class_name not in sch_obj.class_list:
        return False, f'班级:{class_name}不存在'
    class_obj = Class.get_obj(class_name)
    sch_obj.create_course(course_name, period, price)
    class_obj.relate_course(course_name)
    return True, f'课程:{course_name}创建成功'


def create_teacher_interface(sch_name, teacher_name, level, pwd):
    sch_obj = School.get_obj(sch_name)
    if not sch_obj:
        return False, f'学校:{sch_name}不存在'
    if teacher_name in sch_obj.teacher_list:
        return False, f'讲师:{teacher_name}已存在'

    Teacher(sch_name, teacher_name, level, pwd)
    sch_obj.teacher_list.append(teacher_name)
    sch_obj.save_obj(sch_obj)
    return True, f'讲师:{teacher_name}创建成功'


def create_student_interface(sch_name, class_name, stu_name, age, sex, pwd):
    sch_obj = School.get_obj(sch_name)
    if not sch_obj:
        return False, f'学校:{sch_name}不存在'
    class_obj = Class.get_obj(class_name)
    if not class_obj:
        return False, f'班级:{class_name}不存在'
    if stu_name in class_obj.student_list:
        return False, f'学生:{stu_name}已存在'
    Student(sch_name, class_name, stu_name, age, sex, pwd)
    class_obj.student_list.append(stu_name)
    class_obj.save_obj(class_obj)
    return True, f'学生:{stu_name}创建成功'


def show_info_interface(cls_name):
    all_obj = db_handle.get_all_obj(cls_name)
    if not all_obj:
        return False, '信息不存在'

    return True, all_obj

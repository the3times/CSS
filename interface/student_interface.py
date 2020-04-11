from db.models import Student, School, Class
from db import db_handle
import core.login_user



def register_interface(sch_name, class_name, name, pwd, age, sex):
    stu_obj = School.get_obj(sch_name)
    if not stu_obj:
        return False, '学校不存在'
    class_obj = Class.get_obj(class_name)
    if not class_obj:
        return False, '班级不存在'
    all_students = db_handle.get_all_obj(School.__name__)
    if f'{name}.pkl' in all_students:
        return False, '该学生已经存在'
    Student(sch_name, class_name, name, age, sex, pwd)
    class_obj.relate_student(name)
    return True, f'学生:{name}注册成功'



def login_interface(name, pwd):
    stu_obj = Student.get_obj(name)
    if not stu_obj:
        return False, '用户名不存在'
    if pwd != stu_obj.pwd:
        return False, '密码错误'

    core.login_user.login_user[:] = [name]
    return True, '登录成功'


def pay_tuition_interface(amounts):
    stu_name = core.login_user.login_user[0]
    stu_obj = Student.get_obj(stu_name)
    return stu_obj.pay_tuition(float(amounts))


def show_courses_interface():
    stu_name = core.login_user.login_user[0]
    course_list = []
    class_name = Student.get_obj(stu_name).class_name
    class_obj = Class.get_obj(class_name)
    for course in class_obj.course_list:
        course_obj = db_handle.get_obj(course, 'Course')
        course_list.append(course_obj)
    return course_list


def select_course_interface(course_name):
    stu_name = core.login_user.login_user[0]
    stu_obj = Student.get_obj(stu_name)
    if not stu_obj.is_pay_tuition:
        return False, '未交费不能选课'

    if course_name in stu_obj.course:
        return False, f'{course_name}已经加入课程列表，无需再选'
    stu_obj.select_course(course_name)
    return True, f'{course_name}成功添加课程列表'
















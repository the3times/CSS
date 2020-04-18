from db import models


def login_interface(name, pwd):
    role = 'Student'
    from interface import common_interface
    flag, msg = common_interface.common_login_interface(name, pwd, role)
    return flag, msg


def get_my_school_interface(stu_name):
    stu_obj = models.Student.get_obj(stu_name)
    return stu_obj.school


def select_course_interface(course_name, stu_name):
    stu_obj = models.Student.get_obj(stu_name)
    if course_name in stu_obj.check_my_course():
        return False, f'课程: [{course_name}]已经选过，无需再选'
    stu_obj.select_course(course_name)
    return True, f'课程: [{course_name}]选择成功'


def check_my_course_interface(stu_name):
    stu_obj = models.Student.get_obj(stu_name)
    course_list = stu_obj.check_my_course()
    if not course_list:
        return False, '您当前还未选择任何课程'
    return True, course_list


def check_score_interface(stu_name):
    stu_obj = models.Student.get_obj(stu_name)
    score_dict = stu_obj.check_my_score()
    if not score_dict:
        return False, '您当前还未选课课程，没有分数'
    return True, score_dict

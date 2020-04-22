from db import models


def login_interface(name, pwd):
    from interface import common_interface
    role = "Teacher"
    flag, msg = common_interface.common_login_interface(name, pwd, role)
    return flag, msg


def select_course_interface(course_name, teacher_name):
    teacher_obj = models.Teacher.get_obj(teacher_name)
    if course_name in  teacher_obj.course_list:
        return False, f'课程[{course_name}]已经选过，无需再选'
    teacher_obj.select_course(course_name)
    return True, f'课程[{course_name}]选择成功'


def check_my_course_interface(teacher_name):
    teacher_obj = models.Teacher.get_obj(teacher_name)
    course_list = teacher_obj.check_my_courses()
    if not course_list:
        return False, '您还没有选择任何课程'
    return True, course_list


def check_my_student_interface(course_name, teacher_name):
    teacher_obj = models.Teacher.get_obj(teacher_name)
    student_list = teacher_obj.check_my_student(course_name)
    if not student_list:
        return False, f'课程: {course_name} 没有学生选呀'
    return True, student_list


def set_score_interface(stu_name, course_name, score, teacher_name, ):
    teacher_obj = models.Teacher.get_obj(teacher_name)
    teacher_obj.set_score(stu_name, course_name, score)

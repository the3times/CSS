from db import models
from interface import common_interface




def select_school_interface(school_name, stu_name):
    stu_obj = models.Student.get_obj(stu_name)
    if not stu_obj.school:
        stu_obj.select_school(school_name)
        return f'[{school_name}]学校选择成功'
    else:
        return f'[{school_name}]学校已经选择过，无需再选'



def select_course_interface(course_name, stu_name):
    stu_obj = models.Student.get_obj(stu_name)
    if course_name in stu_obj.course_list:
        return f'课程[{course_name}]已经选择过了，无需再选'
    else:
        stu_obj.select_course(course_name)
        return f'[{course_name}]课程选择成功'



def check_score_interface(stu_name):
    stu_obj = models.Student.get_obj(stu_name)
    return stu_obj.score

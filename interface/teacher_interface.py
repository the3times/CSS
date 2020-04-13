from db import models



def select_course_interface(course_name, teacher_name):
    teacher_obj = models.Teacher.get_obj(teacher_name)
    if teacher_obj.course:
        return '您已经选择课程，无须再选'
    else:
        teacher_obj.select_course(course_name)
        return f'[{course_name}]课程选择成功'



def show_student_info_interface(teacher_name):
    teacher_obj = models.Teacher.get_obj(teacher_name)
    if not teacher_obj.course:
        return False, '您还未选择课程'
    student_list = teacher_obj.get_my_student_list()
    if not student_list:
        return False, '没有学生选择该课程'
    stu_info = []
    for stu_name in student_list:
        score = models.Student.get_obj(stu_name).score[teacher_obj.course]
        stu_info.append((stu_name, score))
    return True, stu_info




def set_score_interface(stu_name, score, teacher_name):
    if not score.isdigit():
        return False, '分数必须是整数'

    teacher_obj = models.Teacher.get_obj(teacher_name)
    teacher_obj.set_score(stu_name, score)
    return True, '打分成功'

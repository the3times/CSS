from db import models


def register_interface(name, age, sex):
    admin_obj = models.Admin.get_obj(name)
    if admin_obj:
       return False, f'管理员[{name}]已经存在，无需再次创建'
    models.Admin(name, age, sex)
    return True, f'管理员:[{name}]创建成功'


def login_interface(name, pwd):
    """
    登录接口
    :param name:
    :param pwd: 密码，密文
    :return:
    """
    from interface import common_interface
    role = 'Admin'
    flag, msg = common_interface.common_login_interface(name, pwd, role)
    return flag, msg


def create_school_interface(school_name, school_addr, admin_name):
    school_obj = models.School.get_obj(school_name)
    if school_obj:
        return False, f'学校: [{school_name}]已经存在，无需再创建'
    admin_obj = models.Admin.get_obj(admin_name)
    admin_obj.create_school(school_name, school_addr)
    return True, f'学校:[{school_name}]创建成功'


def create_course_interface(school_name, course_name, course_period, course_price, admin_name):
    school_obj = models.School.get_obj(school_name)
    if course_name in school_obj.course_list:
        return False, f'课程:[{course_name}]已经存在，无需再创建'
    admin_obj = models.Admin.get_obj(admin_name)
    admin_obj.create_course(school_name, course_name, course_period, course_price)
    school_obj.relate_course(course_name)
    return True, f'课程:[{course_name}]创建成功'


def create_teacher_interface(teacher_name, teacher_age, teacher_sex, teacher_level, admin_name):
    teacher_obj = models.Teacher.get_obj(teacher_name)
    if teacher_obj:
        return False, f'老师:[{teacher_name}]已经存在，无需再创建'
    admin_obj = models.Admin.get_obj(admin_name)
    admin_obj.create_teacher(teacher_name, teacher_age, teacher_sex, teacher_level)
    return True, f'老师:[{teacher_name}]创建成功'


def create_student_interface(stu_name, stu_age, stu_sex, school_name, homeland, admin_name):
    stu_obj = models.Student.get_obj(stu_name)
    if stu_obj:
        return False, f'学生:[{stu_name}]已经存在，无需再创建'
    admin_obj = models.Admin.get_obj(admin_name)
    admin_obj.create_student(stu_name, stu_age, stu_sex, school_name, homeland)
    return True, f'学生:[{stu_name}]创建成功'


def reset_user_pwd_interface(name, role, admin_name):
    admin_obj = models.Admin.get_obj(admin_name)
    if hasattr(models, role):
        user_obj = getattr(models, role).get_obj(name)
        if not user_obj:
            return False, '用户不存在'
        admin_obj.reset_user_pwd(name, role)
        return True, '密码重置成功【123456】，请尽快修改'
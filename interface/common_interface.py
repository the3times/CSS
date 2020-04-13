import os
from conf.settings import DB_USER_DIR
from db import models



def login_interface(name, pwd, role):
    role_dict = {
        'Admin': models.Admin,
        'Student': models.Student,
        'Teacher': models.Teacher,
    }
    current_obj = role_dict.get(role).get_obj(name)

    if not current_obj:
        return False, '用户不存在，无法登录'
    if pwd != current_obj.pwd:
        return False, '密码错误'
    else:
        return True, '登录成功'



def edit_pwd_interface(old_pwd, new_pwd, current_user):
    pass



def get_school_list_interface():
    file_dir = os.path.join(DB_USER_DIR, 'School')
    if os.path.exists(file_dir):
        return os.listdir(file_dir)



def get_course_list_interface(current_user):
    if current_user['role'] == 'Student':
        stu_obj = models.Student.get_obj(current_user['name'])
        if not stu_obj.school:
            return []
        return models.School.get_obj(stu_obj.school).course_list

    elif current_user['role'] == 'Teacher':
        file_dir = os.path.join(DB_USER_DIR, 'Course')
        if os.path.exists(file_dir):
            return os.listdir(file_dir)



import os
from conf import settings
from db import models


def get_all_school_list():
    """
    获取所有学校的校名
    :return: 校名列表
    """
    school_folder = os.path.join(settings.DB_USER_DIR, 'School')
    return os.listdir(school_folder)


def get_course_list_from_school(school_name):
    """
    获取一个学校下的所有课程
    :param school_name:
    :return: 课程列表
    """
    school_obj = models.School.get_obj(school_name)
    course_list = school_obj.course_list
    if not course_list:
        return False, '该学校还没有课程，请联系管理员'
    return True, course_list


def common_login_interface(name, pwd, role):
    """
    登录接口
    :param name:
    :param pwd: 密码，密文
    :param role: 角色，如，Admin|Teacher|Student
    :return:
    """
    if hasattr(models, role):
        obj = getattr(models, role).get_obj(name)
        if not obj:
            return False, f'用户名[{name}]不存在'
        if pwd != obj.pwd:
            return False, '用户名或密码错误'
        return True, '登录成功'
    else:
        return False, '您没有权限登录'


def edit_pwd_interface(old_pwd, new_pwd, name, role):
    if hasattr(models, role):
        obj = getattr(models, role).get_obj(name)
        if old_pwd != obj.pwd:
            return False, '旧密码错误，不能修改'
        else:
            obj.pwd = new_pwd
            obj.save_obj()
            return True, '密码修改成功'
    else:
        return False, '您没有权限修改密码'
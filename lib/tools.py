import hashlib
from functools import wraps


def auth(role):
    from core import admin, student, teacher
    role_dict = {
        'admin': admin,
        'student': student,
        'teacher': teacher,
    }
    def wrapper(func):
        @wraps(func)
        def inner(*args, **kwargs):
            if role in role_dict:
                if role_dict.get(role).current_user['name']:
                    res = func(*args, **kwargs)
                    return res
                else:
                    print('您没有登录不能使用此功能')
            else:
                print('您没有权限使用此功能')
        return inner
    return wrapper



def hash_md5(info):
    m = hashlib.md5()
    m.update(info.encode('utf-8'))
    m.update('因为相信所以看见'.encode('utf-8'))
    return m.hexdigest()


def show_school_list(school_list):
    if not school_list:
        print('需要先创建学校再创建课程')
        return False, None
    print('校区列表'.center(10, '='))
    for index, school in enumerate(school_list, 1):
        print(f'({index}) {school}')
    choice = input('请选择课程所在学校的编号：').strip()
    if not choice.isdigit() or int(choice) not in range(1, len(school_list)+1):
        print('请选择合法的学校编号')
        return False, None
    return True, school_list[int(choice) - 1]



def show_course_list(course_list):
    if not course_list:
        print('目前没有课程，，，，')
        return False, None
    print('课程列表'.center(10, '='))
    for index, school in enumerate(course_list, 1):
        print(f'({index}) {school}')
    choice = input('请选择课程的编号：').strip()
    if not choice.isdigit() or int(choice) not in range(1, len(course_list)+1):
        print('请选择合法的课程编号')
        return False, None
    return True, course_list[int(choice) - 1]


def show_student_list(student_info):
    for index, student_info_tuple in enumerate(student_info, 1):
        print(f'({index}) {student_info_tuple[0]} {student_info_tuple[1]}')
    choice = input('请选择学生的编号：').strip()
    if not choice.isdigit() or int(choice) not in range(1, len(student_info)+1):
        print('请选择合法的学生编号')
        return False, None
    return True, student_info[int(choice) - 1][0]
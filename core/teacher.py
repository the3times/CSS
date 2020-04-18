from core.current_user import current_user
from lib.tools import auth, menu_display, is_none, hash_md5, select_item
from interface import teacher_interface, common_interface


def login():
    while 1:
        print('老师登录页面'.center(50, '-'))
        name = input('请输入用户名(Q退出)：').strip()
        if name == 'q':
            break
        pwd = input('请输入密码：').strip()
        if is_none(name, pwd):
            print('用户名或密码不能为空')
            continue
        flag, msg = teacher_interface.login_interface(name, hash_md5(pwd))
        print(msg)
        if flag:
            current_user['name'] = name
            current_user['role'] = 'Teacher'
            break


@auth('Teacher')
def select_course():
    while 1:
        school_list = common_interface.get_all_school_list()
        print('请选择校区'.center(20, '-'))
        success, school_name = select_item(school_list)
        if not success:
            break
        flag, course_list = common_interface.get_course_list_from_school(school_name)
        if not flag:
            print(course_list)
            break
        print('请选择课程'.center(20, '-'))
        success2, course_name = select_item(course_list)
        if not success2:
            break
        flag, msg = teacher_interface.select_course_interface(course_name, current_user['name'])
        print(msg)
        if flag:
            break


@auth('Teacher')
def check_my_course():
    flag, course_list = teacher_interface.check_my_course_interface(current_user['name'])
    print('课程列表：')
    if not flag:
        print(course_list)
    else:
        for index, course_name in enumerate(course_list, 1):
            print(index, course_name)


@auth('Teacher')
def check_my_student():
    while 1:
        flag, course_list = teacher_interface.check_my_course_interface(current_user['name'])
        if not flag:
            print('您还没有选课课程，故没有学生')
            break
        print('课程列表：')
        success, course_name = select_item(course_list)
        if not success:
            break
        flag2, student_list = teacher_interface.check_my_student_interface(course_name, current_user['name'])
        if not flag2:
            print(student_list) # 打印错误信息
        else:
            for index, stu_name in enumerate(student_list, 1):
                print(index, stu_name)
            break


@auth('Teacher')
def set_score_for_student():
    while 1:
        flag, course_list = teacher_interface.check_my_course_interface(current_user['name'])
        if not flag:
            print('您还没有选课课程，故没有学生')
            break
        print('课程列表：')
        success, course_name = select_item(course_list)
        if not success:
            break
        flag2, student_list = teacher_interface.check_my_student_interface(course_name, current_user['name'])
        if not flag2:
            print(student_list) # 打印错误信息，没有学生这选门课
        else:
            flag2, stu_name = select_item(student_list)
            if not flag2:
                break

            score = input('请输入分数：').strip()
            if not score.isdigit():
                print('分数必须是数字')
                continue
            teacher_interface.set_score_interface(stu_name, course_name, score, current_user['name'])
            print('打分成功')



@auth('Teacher')
def edit_my_pwd():
    while 1:
        old_pwd = input('请输入旧密码：').strip()
        new_pwd = input('请设置新密码：').strip()
        re_pwd = input('请确认新密码：').strip()
        if new_pwd != re_pwd:
            print('两次密码输入不一致')
            continue
        flag, msg = common_interface.edit_pwd_interface(
            hash_md5(old_pwd), hash_md5(new_pwd), current_user['name'], current_user['role'])
        print(msg)
        if flag:
            break


def teacher():
    print('这是老师视图页面'.center(50, '-'))
    func_dict = {
        '1': ('登录', login),
        '2': ('选择课程', select_course),
        '3': ('我的课程', check_my_course),
        '4': ('我的学生', check_my_student),
        '6': ('学生打分', set_score_for_student),
        '7': ('修改密码', edit_my_pwd),
    }
    menu_display(func_dict)

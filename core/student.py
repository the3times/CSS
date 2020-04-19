from core.current_user import current_user
from lib.tools import menu_display, auth, is_none, hash_md5, select_item, edit_pwd
from interface import student_interface, common_interface


def login():
    while 1:
        name = input('请输入用户名：').strip().lower()
        if name == 'q':
            break
        pwd = input('请输入密码：').strip()
        if is_none(name, pwd):
            print('用户名或密码不能为空')
            continue
        flag, msg = student_interface.login_interface(name, hash_md5(pwd))
        print(msg)
        if flag:
            current_user['name'] = name
            current_user['role'] = 'Student'
            break


@auth('Student')
def select_course():
    while 1:
        school_name = student_interface.get_my_school_interface(current_user['name'])
        flag, course_list = common_interface.get_course_list_from_school(school_name)
        if not flag:
            print(course_list)
            break
        print('待选课程列表'.center(30, '-'))
        flag2, course_name = select_item(course_list)
        if not flag2:
            break
        flag3, msg = student_interface.select_course_interface(course_name, current_user['name'])
        print(msg)


@auth('Student')
def check_my_course():
    flag, course_list = student_interface.check_my_course_interface(current_user['name'])
    if not flag:
        print(course_list)
        return
    print('您已选课程列表'.center(30, '-'))
    for index, course_name in enumerate(course_list, 1):
        print(index, course_name)


@auth('Student')
def check_my_score():
    flag, score_dict = student_interface.check_score_interface(current_user['name'])
    if not flag:
        print(score_dict)
    else:
        print('课程分数列表')
        for index, course_name in enumerate(score_dict, 1):
            score = score_dict[course_name]
            print(index, course_name, score)


@auth('Student')
def edit_my_pwd():
    edit_pwd(common_interface.edit_pwd_interface, current_user)


def student():
    print('这是学生视图页面'.center(50, '-'))
    func_dict = {
        '1': ('登录', login),
        '2': ('选择课程', select_course),
        '3': ('我的课程', check_my_course),
        '4': ('查看分数', check_my_score),
        '5': ('修改密码', edit_my_pwd),
    }
    menu_display(func_dict)


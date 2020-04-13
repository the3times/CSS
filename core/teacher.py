from lib.tools import auth, hash_md5, show_course_list, show_student_list
from interface import common_interface
from interface import teacher_interface


# 记录当前登录用户
current_user = {'name': None, 'role': 'Teacher'}



def login():
    print('这是老师登录页面'.center(30, '-'))
    while 1:
        teacher_name = input('请输入用户名：').strip()
        pwd = input('请输入密码：').strip()
        flag, msg = common_interface.login_interface(teacher_name, hash_md5(pwd), current_user['role'])
        print(msg)
        if flag:
            current_user['name'] = teacher_name
            break



@auth('teacher')
def select_course():
    course_list = common_interface.get_course_list_interface(current_user)
    while 1:
        flag, course_name = show_course_list(course_list)
        if not flag:
            break
        msg = teacher_interface.select_course_interface(course_name, current_user['name'])
        print(msg)
        break



@auth('teacher')
def show_student():
    print('老师查看学生页面'.center(30, '-'))
    flag, tuple_or_msg = teacher_interface.show_student_info_interface(current_user['name'])
    if not flag:
        print(tuple_or_msg)
        return
    else:
        for index, stu in enumerate(tuple_or_msg, 1):
            print(index, stu[0], stu[1])



@auth('teacher')
def set_score():
    print('这是打分页面'.center(30, '-'))
    flag, tuple_or_msg = teacher_interface.show_student_info_interface(current_user['name'])
    if not flag:
        print(tuple_or_msg)
        return
    while 1:
        success, stu_name = show_student_list(tuple_or_msg)
        score = input('请输入分数：').strip()
        success, msg = teacher_interface.set_score_interface(stu_name, score, current_user['name'])
        print(msg)
        if success:
            break



def teacher():
    print('讲师视图层'.center(50, '-'))
    cmd_func = {
        '1':('登录', login),
        '2':('选择课程', select_course),
        '3':('查看学生', show_student),
        '4':('打分', set_score),
    }
    while 1:
        for k, v in cmd_func.items():
            print(f'({k}) {v[0]}', end='\t')
        choice = input('\n请选择功能的编号(Q退出)：').strip().lower()
        if choice == 'q':
            break
        if choice not in cmd_func:
            print('您选择的编号不存在，请重新选择')
            continue
        cmd = cmd_func.get(choice)[1]
        cmd()
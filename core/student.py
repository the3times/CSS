from lib.tools import auth, hash_md5, show_school_list, show_course_list
from interface import student_interface
from interface import common_interface



# 记录当前登录用户
current_user = {'name': None, 'role': 'Student'}



def login():
    print('这是学生登录页面'.center(30, '-'))
    while 1:
        name = input('请输入用户名：').strip()
        pwd = input('请输入密码：').strip()
        flag, msg = common_interface.login_interface(name, hash_md5(pwd), current_user['role'])
        print(msg)
        if flag:
            current_user['name'] = name
            break



@auth('student')
def select_school():
    print('这是学生选择学校页面'.center(30, '-'))
    school_list = common_interface.get_school_list_interface()
    flag, school_name = show_school_list(school_list)
    if not flag:
        return
    # 学校存在时
    msg = student_interface.select_school_interface(school_name, current_user['name'])
    print(msg)



@auth('student')
def select_course():
    print('这是学生选择课程页面'.center(30, '-'))
    course_list = common_interface.get_course_list_interface(current_user)
    flag, course_name = show_course_list(course_list)
    if not flag:
       return
    msg = student_interface.select_course_interface(course_name, current_user['name'])
    print(msg)



@auth('student')
def check_score():
    print('这是学生查看分数页面'.center(30, '-'))
    score_dict = student_interface.check_score_interface(current_user['name'])
    print('分数列表：')
    for course_name, score in score_dict.items():
        print(f'{course_name}： {score}')




def student():
    print('学生视图层'.center(50, '-'))
    cmd_func = {
        '1':('登录', login),
        '2':('选择学校', select_school),
        '3':('选择课程', select_course),
        '4':('查看分数', check_score),
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
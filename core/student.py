from lib.tools import auth, hash_md5
from interface.student_interface import login_interface
from interface.student_interface import register_interface
from interface.student_interface import pay_tuition_interface
from interface.student_interface import show_courses_interface
from interface.student_interface import select_course_interface



def register():
    print('学生登录页面'.center(50, '-'))
    while 1:
        sch_name = input('请输入学校名字：').strip()
        class_name = input('请输入班级名字：').strip()
        name = input('请输入您的用户名：').strip()
        pwd = input('请输入您的密码：').strip()
        re_pwd = input('请确认密码：').strip()
        age = input('请输入您的年龄：').strip()
        sex = input('请输入您的性别：').strip()
        if pwd != re_pwd:
            return False, '两次密码输入不一致'
        flag, msg = register_interface(sch_name, class_name, name, hash_md5(pwd), age, sex)
        print(msg)
        if flag: break



def login():
    print('学生登录页面'.center(50, '-'))
    while 1:
        name = input('请输入您的用户名：').strip()
        pwd = input('请输入您的密码：').strip()
        flag, msg = login_interface(name, hash_md5(pwd))
        print(msg)
        if flag: break



@auth
def pay_tuition():
    print('学生缴费页面'.center(50, '-'))
    while 1:
        amounts = input('请输入缴费金额：').strip()
        if not amounts.isdigit():
            continue
        flag, msg = pay_tuition_interface(amounts)
        print(msg)
        if flag:
            break



@auth
def select_course():
    print('学生选课页面'.center(50, '-'))
    course_obj_list = show_courses_interface()
    while 1:
        for index, course in enumerate(course_obj_list, 1):
            print(index, course)
        choice = input('请选择课程编号：').strip()
        if not choice.isdigit() or int(choice) not in range(1, len(course_obj_list) + 1):
            continue
        course_name = course_obj_list[int(choice)-1].name
        flag, msg = select_course_interface(course_name)
        print(msg)
        if flag: break



@auth
def show_my_course():
    pass


@auth
def show_my_score():
    pass




def student():
    cmd_func = {
        '1': ('登录', login),
        '2': ('注册', register),
        '3': ('缴费', pay_tuition),
        '4': ('选择课程', select_course),
        '5': ('我的课程', show_my_course),
        '6': ('我的分数', show_my_score),
    }
    while 1:
        for k, v in cmd_func.items():
            print(f'\t({k}) {v[0]}', end='\t')

        cmd = input('\n请选择功能编号(Q退出)：').strip().lower()
        if cmd == 'q': break
        if cmd not in cmd_func:
            print('请选择合法的功能编号')
            continue
        func = cmd_func.get(cmd)[1]
        func()
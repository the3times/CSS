from lib.tools import hash_md5, auth, show_school_list
from interface import admin_interface
from interface import common_interface


# 记录当前登录用户
current_user = {'name': None, 'role': 'Admin'}


def register():
    print('这是管理员注册页面'.center(30, '-'))
    while 1:
        name = input('请设置管理员名字：').strip()
        flag, msg = admin_interface.register_interface(name)
        print(msg)
        if flag:
            break


def login():
    print('这是管理员登录页面'.center(30, '-'))
    while 1:
        name = input('请输入用户名：').strip()
        pwd = input('请输入密码：').strip()
        flag, msg = common_interface.login_interface(name, hash_md5(pwd), current_user['role'])
        print(msg)
        if flag:
            current_user['name'] = name
            break


@auth('admin')
def create_school():
    print('这是创建学校页面'.center(30, '-'))
    while 1:
        name = input('请设置学校名字(Q退出)：').strip().lower()
        if name == 'q':
            break
        addr = input('请设置学校地址：').strip()
        flag, msg = admin_interface.create_school_interface(name, addr, current_user['name'])
        print(msg)
        if flag:
            break


@auth('admin')
def create_course():
    print('这是创建课程页面'.center(30, '-'))
    school_list = common_interface.get_school_list_interface()
    while 1:
        flag, school_name = show_school_list(school_list)
        if not flag:
            continue
        # 学校存在时
        course_name = input('请设置课程名称：').strip()
        course_period = input('请设置课程周期(月)：').strip()
        course_price = input('请设置课程价格(元)：').strip()
        if not course_period.isdigit() or not course_price.isdigit():
            print('课程周期和价格都是整数哦')
            continue
        msg = admin_interface.create_course_interface(
            school_name, course_name, course_period, course_price, current_user['name'])
        print(msg)
        break


@auth('admin')
def create_teacher():
    print('这是创建老师页面'.center(30, '-'))
    while 1:
        teacher_name = input('请设置老师姓名(Q退出)：').strip().lower()
        if teacher_name == 'q':
            break
        flag, msg = admin_interface.create_teacher_interface(teacher_name, current_user['name'])
        print(msg)
        if flag:
            break


@auth('admin')
def create_student():
    print('这是创建学生页面'.center(30, '-'))
    while 1:
        stu_name = input('请设置学生姓名(Q退出)：').strip().lower()
        if stu_name == 'q':
            break
        flag, msg = admin_interface.create_student_interface(stu_name, current_user['name'])
        print(msg)
        if flag:
            break


@auth('admin')
def edit_password():
    print('这是修改密码页面'.center(30, '-'))
    while 1:
        pwd = input('请输入原密码：').strip()
        new_pwd = input('请设置新密码：').strip()
        re_pwd = input('请确认密码：').strip()
        if new_pwd != re_pwd:
            print('确认密码与新密码不一致')
            continue
        flag, msg = common_interface.edit_pwd_interface(hash_md5(pwd), hash_md5(new_pwd), current_user)
        print(msg)
        if flag:
            break



def admin():
    print('管理员视图层'.center(50, '-'))
    cmd_func = {
        '1':('登录', login),
        '2':('注册', register),
        '3':('创建学校', create_school),
        '4':('创建课程', create_course),
        '5':('创建讲师', create_teacher),
        '6':('创建学生', create_student),
        # '7':('修改密码', edit_password),
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
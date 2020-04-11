from lib.tools import hash_md5, auth
from interface.admin_interface import register_interface
from interface.admin_interface import login_interface
from interface.admin_interface import create_school_interface
from interface.admin_interface import create_class_interface
from interface.admin_interface import create_course_interface
from interface.admin_interface import create_teacher_interface
from interface.admin_interface import create_student_interface
from interface.admin_interface import show_info_interface



def register():
    print('管理员注册页面'.center(50, '-'))
    while 1:
        name = input('用户名：').strip()
        pwd = input('密码：').strip()
        re_pwd= input('确认密码：').strip()
        if pwd != re_pwd:
            print('两次密码输入不一致')
            continue
        flag, msg = register_interface(name, hash_md5(pwd))
        print(msg)
        if flag: break


def login():
    print('管理员登录页面'.center(50, '-'))
    while 1:
        name = input('用户名：').strip()
        pwd = input('密码：').strip()

        flag, msg = login_interface(name, hash_md5(pwd))
        print(msg)
        if flag: break


@auth
def create_school():
    print('创建学校页面'.center(50, '-'))
    while 1:
        sch_name = input('请输入学校名字：').strip()
        sch_addr = input('请输入学校地址：').strip()
        flag, msg = create_school_interface(sch_name, sch_addr)
        print(msg)
        if flag: break


@auth
def create_class():
    print('创建班级页面'.center(50, '-'))
    while 1:
        sch_name = input('请选择班级所在学校：').strip()
        class_name = input('请输入班级的名字：').strip()
        flag, msg = create_class_interface(sch_name, class_name)
        print(msg)
        if flag: break


@auth
def create_course():
    print('创建课程页面'.center(50, '-'))
    while 1:
        sch_name = input('请选择课程所在学校：').strip()
        class_name = input('请选择课程所在班级：').strip()
        course_name = input('请输入课程的名字：').strip()
        period = input('请输入课程的周期：').strip()
        price = input('请输入课程的价格：').strip()

        flag, msg = create_course_interface(sch_name, class_name, course_name, period, price)
        print(msg)
        if flag: break


@auth
def create_teacher():
    print('创建讲师页面'.center(50, '-'))
    while 1:
        sch_name = input('请选择讲师所在学校：').strip()
        teacher_name = input('请输入讲师的名字：').strip()
        level = input('请输入讲师的级别：').strip()
        pwd = input('请设置讲师的密码：').strip()
        re_pwd = input('请确认密码：').strip()
        if pwd != re_pwd:
            print('两次密码输入不一致')
            continue
        flag, msg = create_teacher_interface(sch_name, teacher_name, level, hash_md5(pwd))
        print(msg)
        if flag: break


@auth
def create_student():
    print('创建学生页面'.center(50, '-'))
    while 1:
        sch_name = input('请选择学生所在学校：').strip()
        class_name = input('请选择学生所在班级：').strip()
        stu_name = input('请输入学生的名字：').strip()
        age = input('请输入学生的年龄：').strip()
        sex = input('请输入学生的性别：').strip()
        pwd = input('请设置学生的密码：').strip()
        re_pwd = input('请确认密码：').strip()
        if pwd != re_pwd:
            print('两次密码输入不一致')
            continue
        flag, msg = create_student_interface(sch_name, class_name, stu_name, age, sex, hash_md5(pwd))
        print(msg)
        if flag: break


@auth
def show_info():
    info_dict = {
        '1': ('校区信息', 'School'),
        '2': ('班级信息', 'Class'),
        '3': ('课程信息', 'Course'),
        '4': ('讲师信息', 'Teacher'),
        '5': ('学生信息', 'Student'),
    }
    while 1:
        for k, v in info_dict.items():
            print(k, v[0])

        info = input('请选择查看的信息编号(Q返回)：').strip().lower()
        if info == 'q': break
        if info not in info_dict:
            continue
        cls_name = info_dict.get(info)[1]
        flag, obj_list = show_info_interface(cls_name)
        if flag:
            for obj in obj_list:
                print(obj)
        else:
            print(f'{cls_name}不存在')


def admin():
    cmd_func = {
        '1': ('登录', login),
        '2': ('注册', register),
        '3': ('查看信息', show_info),
        '4': ('创建学校', create_school),
        '5': ('创建班级', create_class),
        '6': ('创建课程', create_course),
        '7': ('创建老师', create_teacher),
        '8': ('创建学生', create_student),
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
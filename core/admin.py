from lib.tools import hash_md5, is_none, auth, select_item
from core.current_user import current_user
from interface import admin_interface, common_interface



def login():
    print('这是登录页面'.center(50, '-'))
    while 1:
        name = input('请输入用户名(Q退出)：').strip().lower()
        if name == 'q':
            break
        pwd = input('请输入密码：').strip()
        if not is_none(name, pwd):
            print('用户名或密码不能为空')
            continue
        flag, msg = admin_interface.login_interface(name, hash_md5(pwd))
        print(msg)
        if flag:
            current_user['name'] = name
            current_user['role'] = 'Admin'
            break



def register():
    print('这是注册页面'.center(50, '-'))
    while 1:
        name = input('设置管理员名字(Q退出)：').strip().lower()
        if name == 'q':
            break
        if not is_none(name):
            print('用户名不能为空')
            continue
        age = input('设置管理员年龄：').strip()
        if not age.isdigit():
            print('年龄设置不合法')
            continue
        sex = input('设置管理员性别：').strip()
        if sex not in ('male', 'female'):
            print('性别必须是：male or female')
            continue

        flag, msg = admin_interface.register_interface(name, age, sex)
        print(msg)
        if flag:
            break


@auth('Admin')
def create_school():
    print('创建学校页面'.center(50, '-'))
    while 1:
        school_name = input('请设置学校名字(Q退出)：').strip().lower()
        if school_name =='q':
            break
        school_addr = input('请设置学校地址：').strip()
        if not is_none(school_name, school_addr):
            print('学校名或地址不能为空')
            continue
        flag, msg = admin_interface.create_school_interface(
            school_name, school_addr, current_user['name'])
        print(msg)
        if flag:
            break


@auth('Admin')
def create_course():
    print('创建课程页面'.center(50, '-'))
    while 1:
        school_list = common_interface.get_all_school_list()
        success, school_name = select_item(school_list)
        if not success:
            break
        course_name = input('请设置课程名(Q退出)：').strip().lower()
        if course_name == 'q':
            break
        course_period = input('请设置课程周期：').strip()
        course_price = input('请设置课程价格：').strip()
        if not is_none(course_name, course_period, course_price):
            print('课程名称，课程周期，课程价格不能为空')
            continue
        flag, msg = admin_interface.create_course_interface(
            school_name, course_name, course_period, course_price, current_user['name'])
        print(msg)
        if flag:
            break



@auth('Admin')
def create_teacher():
    print('创建老师页面'.center(50, '-'))
    while 1:
        name = input('请输入老师名字(Q退出)：').strip().lower()
        if name == 'q':
            break
        if not is_none(name):
            print('用户名不能为空')
            continue
        age = input('请输入老师年龄：').strip()
        if not age.isdigit():
            print('年龄设置不合法')
            continue
        sex = input('请输入老师性别：').strip()
        if sex not in ('male', 'female'):
            print('性别必须是：male or female')
            continue
        level = input('请输入老师级别：').strip()
        flag, msg = admin_interface.create_teacher_interface(name, age, sex, level, current_user['name'])
        print(msg)
        if flag:
            break



@auth('Admin')
def create_student():
    print('创建学生页面'.center(50, '-'))
    while 1:
        school_list = common_interface.get_all_school_list()
        success, school_name = select_item(school_list)
        if not success:
            break
        name = input('请输入学生名字(Q退出)：').strip().lower()
        if name == 'q':
            break
        age = input('请输入学生年龄：').strip()
        if not age.isdigit():
            print('年龄设置不合法')
            continue
        sex = input('请输入学生性别：').strip()
        if sex not in ('male', 'female'):
            print('性别必须是：male or female')
            continue
        homeland = input('请输入学生的籍贯：').strip()
        if not is_none(name, homeland):
            print('学生名或籍贯不能为空')
            continue

        flag, msg = admin_interface.create_student_interface(
            name, age, sex, school_name, homeland, current_user['name'])
        print(msg)
        if flag:
            break



def admin():
    print('这是管理员视图页面'.center(50, '-'))
    func_dict = {
        '1': ('登录', login),
        '2': ('注册', register),
        '3': ('创建学校', create_school),
        '4': ('创建课程', create_course),
        '5': ('创建老师', create_teacher),
        '6': ('创建学生', create_student),
    }
    while 1:
        for k, v in func_dict.items():
            print(f'({k}) {v[0]}', end='\t')

        func_choice = input('\n请输入选择的功能编号(Q退出)：').strip().lower()
        if func_choice == 'q':
            break
        if func_choice not in func_dict:
            continue
        func = func_dict.get(func_choice)[1]
        func()
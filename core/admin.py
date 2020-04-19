from core.baseview import BaseViewer as Base
from lib.tools import ToolsMixin
from interface import admin_interface, common_interface


class AdminViewer(ToolsMixin, Base):

    @Base.my_func('登录')
    def login(self):
        Base.role = 'Admin'
        super().login(admin_interface)

    @Base.my_func('注册')
    def register(self):
        print('这是注册页面'.center(50, '-'))
        while 1:
            name = input('设置管理员名字(Q退出)：').strip().lower()
            if name == 'q':
                break
            if self.is_none(name):
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


    @Base.my_func('创建学校')
    @Base.auth('Admin')
    def create_school(self):
        print('创建学校页面'.center(50, '-'))
        while 1:
            school_name = input('请设置学校名字(Q退出)：').strip().lower()
            if school_name =='q':
                break
            school_addr = input('请设置学校地址：').strip()
            if self.is_none(school_name, school_addr):
                print('学校名或地址不能为空')
                continue
            flag, msg = admin_interface.create_school_interface(
                school_name, school_addr, self.name)
            print(msg)
            if flag:
                break


    @Base.my_func('创建课程')
    @Base.auth('Admin')
    def create_course(self):
        print('创建课程页面'.center(50, '-'))
        while 1:
            school_list = common_interface.get_all_school_list()
            success, school_name = self.select_item(school_list)
            if not success:
                break
            course_name = input('请设置课程名(Q退出)：').strip().lower()
            if course_name == 'q':
                break
            course_period = input('请设置课程周期：').strip()
            course_price = input('请设置课程价格：').strip()
            if self.is_none(course_name, course_period, course_price):
                print('课程名称，课程周期，课程价格不能为空')
                continue
            flag, msg = admin_interface.create_course_interface(
                school_name, course_name, course_period, course_price, self.name)
            print(msg)
            if flag:
                break


    @Base.my_func('创建老师')
    @Base.auth('Admin')
    def create_teacher(self):
        print('创建老师页面'.center(50, '-'))
        while 1:
            name = input('请输入老师名字(Q退出)：').strip().lower()
            if name == 'q':
                break
            if self.is_none(name):
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
            flag, msg = admin_interface.create_teacher_interface(name, age, sex, level, self.name)
            print(msg)
            if flag:
                break


    @Base.my_func('创建老师')
    @Base.auth('Admin')
    def create_student(self):
        print('创建学生页面'.center(50, '-'))
        while 1:
            school_list = common_interface.get_all_school_list()
            success, school_name = self.select_item(school_list)
            if not success:
                break
            name = input('请学生名字(Q退出)：').strip().lower()
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
            if self.is_none(name, homeland):
                print('学生名或籍贯不能为空')
                continue

            flag, msg = admin_interface.create_student_interface(
                name, age, sex, school_name, homeland, self.name)
            print(msg)
            if flag:
                break


    @Base.my_func('修改密码')
    @Base.auth('Admin')
    def edit_my_pwd(self):
        self.edit_pwd(common_interface.edit_pwd_interface)


    @Base.my_func('重置密码')
    @Base.auth('Admin')
    def reset_user_pwd(self):
        while 1:
            name = input('请输入用户名字：').strip().lower()
            if name == 'q':
                break
            role = input('请输入用户角色：').strip()
            if role not in ['Student', 'Teacher', 'Admin']:
                print('用户角色不存在')
                continue
            flag, msg = admin_interface.reset_user_pwd_interface(name, role, self.name)
            print(msg)
            if flag:
                break
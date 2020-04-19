from core.baseview import BaseViewer as Base
from lib.tools import ToolsMixin
from interface import teacher_interface, common_interface


class TeacherViewer(ToolsMixin, Base):

    @Base.my_func('登录')
    def login(self):
        Base.role = 'Teacher'
        super().login(teacher_interface)

    @Base.my_func('选择课程')
    @Base.auth('Teacher')
    def select_course(self):
        while 1:
            school_list = common_interface.get_all_school_list()
            print('请选择校区'.center(20, '-'))
            success, school_name = self.select_item(school_list)
            if not success:
                break
            flag, course_list = common_interface.get_course_list_from_school(school_name)
            if not flag:
                print(course_list)
                break
            print('请选择课程'.center(20, '-'))
            success2, course_name = self.select_item(course_list)
            if not success2:
                break
            flag, msg = teacher_interface.select_course_interface(course_name, self.name)
            print(msg)
            if flag:
                break

    @Base.my_func('我的课程')
    @Base.auth('Teacher')
    def check_my_course(self):
        flag, course_list = teacher_interface.check_my_course_interface(self.name)
        if not flag:
            print(course_list)
        else:
            print('我的课程：')
            for index, course_name in enumerate(course_list, 1):
                print(index, course_name)

    @Base.my_func('我的学生')
    @Base.auth('Teacher')
    def check_my_student(self):
        while 1:
            flag, course_list = teacher_interface.check_my_course_interface(self.name)
            if not flag:
                print('您还没有选课课程，故没有学生')
                break
            print('我的课程：')
            success, course_name = self.select_item(course_list)
            if not success:
                break
            flag2, student_list = teacher_interface.check_my_student_interface(course_name, self.name)
            if not flag2:
                print(student_list) # 打印错误信息
            else:
                print('我的学生')
                for index, stu_name in enumerate(student_list, 1):
                    print(index, stu_name)
                break


    @Base.my_func('打分')
    @Base.auth('Teacher')
    def set_score_for_student(self):
        while 1:
            flag, course_list = teacher_interface.check_my_course_interface(self.name)
            if not flag:
                print('您还没有选课课程，故没有学生')
                break
            print('我的课程：')
            success, course_name = self.select_item(course_list)
            if not success:
                break
            flag2, student_list = teacher_interface.check_my_student_interface(course_name, self.name)
            if not flag2:
                print(student_list) # 打印错误信息，没有学生这选门课
            else:
                print('我的学生')
                flag2, stu_name = self.select_item(student_list)
                if not flag2:
                    break
                score = input('请输入分数：').strip()
                if not score.isdigit():
                    print('分数必须是数字')
                    continue
                teacher_interface.set_score_interface(stu_name, course_name, score, self.name)
                print('打分成功')


    @Base.my_func('修改密码')
    @Base.auth('Teacher')
    def edit_my_pwd(self):
        self.edit_pwd(common_interface.edit_pwd_interface)


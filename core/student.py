from core.baseview import BaseViewer as Base
from lib.tools import ToolsMixin
from interface import student_interface, common_interface


class StudentViewer(ToolsMixin, Base):

    @Base.my_func('登录')
    def login(self):
        Base.role = 'Student'
        super().login(student_interface)


    @Base.my_func('选择课程')
    @Base.auth('Student')
    def select_course(self):
        while 1:
            school_name = student_interface.get_my_school_interface(self.name)
            flag, course_list = common_interface.get_course_list_from_school(school_name)
            if not flag:
                print(course_list)
                break
            print('待选课程列表'.center(30, '-'))
            flag2, course_name = self.select_item(course_list)
            if not flag2:
                break
            flag3, msg = student_interface.select_course_interface(course_name, self.name)
            print(msg)


    @Base.my_func('我的课程')
    @Base.auth('Student')
    def check_my_course(self):
        flag, course_list = student_interface.check_my_course_interface(self.name)
        if not flag:
            print(course_list)
            return
        print('我的课程：'.center(30, '-'))
        for index, course_name in enumerate(course_list, 1):
            print(index, course_name)


    @Base.my_func('我的分数')
    @Base.auth('Student')
    def check_my_score(self):
        flag, score_dict = student_interface.check_score_interface(self.name)
        if not flag:
            print(score_dict)
        else:
            print('课程分数列表')
            for index, course_name in enumerate(score_dict, 1):
                score = score_dict[course_name]
                print(index, course_name, score)


    @Base.my_func('修改密码')
    @Base.auth('Student')
    def edit_my_pwd(self):
        self.edit_pwd(common_interface.edit_pwd_interface)




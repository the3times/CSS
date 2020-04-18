from core.admin import admin
from core.student import student
from core.teacher import teacher
from lib.tools import menu_display


def css():
    view_dict = {
        '1': ('学生', student),
        '2': ('老师', teacher),
        '3': ('管理员', admin),
    }
    menu_display(view_dict)
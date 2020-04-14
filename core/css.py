from core.admin import admin
from core.student import student
from core.teacher import teacher



def css():
    view_dict = {
        '1': ('学生', student),
        '2': ('老师', teacher),
        '3': ('管理员', admin),
    }
    while 1:
        for k, v in view_dict.items():
            print(f'({k}) {v[0]}', end='\t')
        view_choice = input('\n请输入您的角色编号(Q退出)：').strip().lower()
        if view_choice == 'q':
            exit()
        if view_choice not in view_dict:
            continue
        view_role = view_dict.get(view_choice)[1]
        view_role()
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
            print(f'\t({k}) {v[0]}', end='\t')

        your_viewer = input('\n请选择您的角色：').strip()
        if your_viewer not in view_dict:
            print('请选择合适的角色编号')
            continue
        view = view_dict.get(your_viewer)[1]
        view()
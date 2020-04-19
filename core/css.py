from core.student import StudentViewer
from core.teacher import TeacherViewer
from core.admin import AdminViewer


def css():
    view_dict = {
        '1': ('学生', StudentViewer),
        '2': ('老师', TeacherViewer),
        '3': ('管理员', AdminViewer),
    }
    while 1:
        for k, v in view_dict.items():
            print(f'({k}){v[0]}', end='\t')
        view = input("\n>>>：").strip()
        if view == 'q':
            break
        if view not in view_dict:
            continue
        viewer = view_dict.get(view)[1]()
        viewer.start()
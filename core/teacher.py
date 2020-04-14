from core.current_user import current_user



def login():
    pass


def select_course():
    pass


def check_my_course():
    pass


def check_my_student():
    pass


def set_score_for_student():
    pass



def teacher():
    print('这是老师视图页面'.center(50, '-'))
    func_dict = {
        '1': ('登录', login),
        '2': ('选择课程', select_course),
        '3': ('我的课程', check_my_course),
        '4': ('我的学生', check_my_student),
        '6': ('打分', set_score_for_student),
    }
    while 1:
        for k, v in func_dict.items():
            print(f'({k}) {v[0]}', end='\t')

        func_choice = input('请输入选择的功能编号(Q退出)：').strip().lower()
        if func_choice == 'q':
            break
        if func_choice not in func_dict:
            continue
        func = func_dict.get(func_choice)[1]
        func()

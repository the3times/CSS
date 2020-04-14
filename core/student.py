from core.current_user import current_user


def login():
    pass


def select_school():
    pass


def select_course():
    pass


def pay_tuition():
    pass



def check_score():
    pass



def student():
    print('这是学生视图页面'.center(50, '-'))
    func_dict = {
        '1': ('登录', login),
        '2': ('选择校区', select_school),
        '3': ('选择课程', select_course),
        '4': ('课程缴费', pay_tuition),
        '6': ('查看分数', check_score),
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

